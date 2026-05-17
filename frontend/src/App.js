import React from "react";
import Sidebar from "./Sidebar";
import Dashboard from "./Dashboard";

function App() {
  return (
    <div style={{ display: "flex", minHeight: "100vh", background: "#0f172a" }}>
      <Sidebar />
      <Dashboard />
    </div>
  );
}

export default App;
