import React from "react";
import "./Dashboard.css";

import Header from "../components/Header";
import InteractionForm from "../components/InteractionForm";
console.log(InteractionForm);
import AIChat from "../components/AIChat";

const Dashboard = () => {
  return (
    <div className="dashboard">

      <Header />

      <div className="content">

        <div className="left-panel">
          <InteractionForm />
        </div>

        <div className="right-panel">
          <AIChat />
        </div>

      </div>

    </div>
  );
};

export default Dashboard;