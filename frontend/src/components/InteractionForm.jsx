import React from "react";
import { useSelector } from "react-redux";
import api from "../services/api";
import "./InteractionForm.css";

const InteractionForm = () => {
  const data = useSelector((state) => state.interaction);

  console.log("InteractionForm Redux:", JSON.stringify(data, null, 2));

 const handleSave = async () => {
  try {
    const isValidDate = /^\d{4}-\d{2}-\d{2}$/.test(
      data.interaction_date || ""
    );

    const payload = {
      hcp_name: data.hcp_name || "",
      interaction_type: data.interaction_type || "Meeting",

      interaction_date: isValidDate
        ? data.interaction_date
        : null,

      interaction_time:
        data.interaction_time &&
        /^\d{2}:\d{2}$/.test(data.interaction_time)
          ? data.interaction_time
          : null,

      attendees: data.attendees || "",
      topics_discussed: data.topics_discussed || "",
      materials_shared: data.materials_shared || "",
      samples_distributed: data.samples_distributed || "",
      sentiment: data.sentiment || "Neutral",
      outcomes: data.outcomes || "",
      follow_up: data.follow_up || "",
    };

    console.log(
      "Saving Payload:",
      JSON.stringify(payload, null, 2)
    );

    const response = await api.post("/interaction/", payload);

    console.log("Saved:", response.data);
    alert("Interaction saved successfully!");
  } catch (error) {
    console.error(
      "Backend Error:",
      error.response?.data || error.message
    );

    alert(
      error.response?.data?.detail
        ? JSON.stringify(error.response.data.detail)
        : "Failed to save interaction."
    );
  }
};

    return (
    <div className="interaction-card">

      <div className="form-header">
        <h2>Interaction Details</h2>
        <span className="status-badge">AI Assisted</span>
      </div>

      {/* HCP */}

      <div className="field">
        <label>Healthcare Professional (HCP)</label>

        <div className="search-box">
          <input
            value={data.hcp_name}
            placeholder="Search or Select HCP"
            readOnly
          />

          <button
            type="button"
            className="small-btn"
            onClick={() => alert("Search feature coming soon")}
          >
            Search
          </button>
        </div>
      </div>

      {/* Type + Date */}

      <div className="row">

        <div className="field">
          <label>Interaction Type</label>

          <input
            value={data.interaction_type}
            placeholder="Meeting"
            readOnly
          />
        </div>

        <div className="field">
          <label>Interaction Date</label>

          <input
            value={data.interaction_date || ""}
            placeholder="Date"
            readOnly
          />
        </div>

      </div>

      {/* Time + Attendees */}

      <div className="row">

        <div className="field">
          <label>Interaction Time</label>

          <input
            value={data.interaction_time || ""}
            placeholder="Time"
            readOnly
          />
        </div>

        <div className="field">
          <label>Attendees</label>

          <input
            value={data.attendees}
            placeholder="Enter attendees"
            readOnly
          />
        </div>

      </div>

      {/* Topics */}

      <div className="field">
        <label>Topics Discussed</label>

        <textarea
          rows="4"
          value={data.topics_discussed}
          placeholder="Describe discussion..."
          readOnly
        />
      </div>

      {/* Materials */}

      <div className="field">

        <label>Materials Shared</label>

        <div className="search-box">

          <input
            value={data.materials_shared}
            placeholder="Materials"
            readOnly
          />

          <button
            type="button"
            className="small-btn"
            onClick={() => alert("Add Materials")}
          >
            + Add
          </button>

        </div>

      </div>
            {/* Samples */}

      <div className="field">

        <label>Samples Distributed</label>

        <div className="search-box">

          <input
            value={data.samples_distributed}
            placeholder="Samples"
            readOnly
          />

          <button
            type="button"
            className="small-btn"
            onClick={() => alert("Add Samples")}
          >
            + Add
          </button>

        </div>

      </div>

      {/* Sentiment */}

      <div className="field">

        <label>Observed / Inferred HCP Sentiment</label>

        <div className="radio-group">

          <label className="radio-item">
            <input
              type="radio"
              checked={data.sentiment === "Positive"}
              readOnly
            />
            Positive
          </label>

          <label className="radio-item">
            <input
              type="radio"
              checked={data.sentiment === "Neutral"}
              readOnly
            />
            Neutral
          </label>

          <label className="radio-item">
            <input
              type="radio"
              checked={data.sentiment === "Negative"}
              readOnly
            />
            Negative
          </label>

        </div>

      </div>

      {/* Outcomes */}

      <div className="field">

        <label>Outcomes</label>

        <textarea
          rows="4"
          value={data.outcomes}
          placeholder="Interaction outcome..."
          readOnly
        />

      </div>

      {/* Follow Up */}

      <div className="field">

        <label>Follow-up Action</label>

        <textarea
          rows="4"
          value={data.follow_up}
          placeholder="Follow-up plan..."
          readOnly
        />

      </div>

      <button
        className="save-btn"
        onClick={handleSave}
      >
        💾 Save Interaction
      </button>

    </div>
  );
};

export default InteractionForm;