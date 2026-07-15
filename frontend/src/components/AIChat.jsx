import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { updateInteraction } from "../redux/interactionSlice";
import api from "../services/api";
import "../styles/AIChat.css";

const AIChat = () => {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const dispatch = useDispatch();

  useEffect(() => {
    setChat([
      {
        sender: "bot",
        text: "👋 Hello! Describe your interaction with the Healthcare Professional, and I'll automatically fill the CRM form.",
      },
    ]);
  }, []);

  const sendMessage = async () => {
    if (!message.trim()) return;

    // Show user's message
    setChat((prev) => [
      ...prev,
      {
        sender: "user",
        text: message,
      },
    ]);

    try {
      const response = await api.post("/agent/chat", {
        message,
      });

      const data = response.data;

      console.log("API Response:", JSON.stringify(data, null, 2));

      let botMessage = "";

      // Interaction JSON received
      if (data.hcp_name !== undefined) {
        dispatch(updateInteraction(data));

        botMessage = `✅ Interaction logged successfully!

HCP Name: ${data.hcp_name || "-"}
Interaction Type: ${data.interaction_type || "-"}
Date: ${data.interaction_date || "-"}
Attendees: ${data.attendees || "-"}
Topics Discussed: ${data.topics_discussed || "-"}
Sentiment: ${data.sentiment || "-"}
Follow-up: ${data.follow_up || "-"}

The interaction form has been updated automatically.`;
      }

      // Normal AI response
      else if (data.raw_response) {
        botMessage = data.raw_response;
      }

      // Fallback
      else {
        botMessage = "✅ Request completed successfully.";
      }

      setChat((prev) => [
        ...prev,
        {
          sender: "bot",
          text: botMessage,
        },
      ]);
    } catch (error) {
      console.error(error);

      setChat((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "❌ Sorry, something went wrong. Please try again.",
        },
      ]);
    }

    setMessage("");
  };

  return (
    <div className="chat-card">
      <h2>🤖 AI CRM Assistant</h2>

      <div className="chat-window">
        {chat.map((item, index) => (
          <div key={index} className={item.sender}>
            {item.text}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          className="chat-input"
          type="text"
          value={message}
          placeholder="Describe your interaction..."
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button onClick={sendMessage}>
          AI Log
        </button>
      </div>
    </div>
  );
};

export default AIChat;