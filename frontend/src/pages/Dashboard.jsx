import React, { useEffect, useState } from "react";
import ThreatGraph from "./ThreatGraph";

function Dashboard() {
  const [threats, setThreats] = useState(128);
  const [criticalAlerts, setCriticalAlerts] = useState(18);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/threats/live")
      .then((response) => response.json())
      .then((data) => {
        setThreats(data.threats || 128);
        setCriticalAlerts(data.critical || 18);
      })
      .catch((error) => {
        console.error("API error:", error);
      });
  }, []);

  return (
    <div style={styles.main}>
      <h1>Cyber Threat Detection Dashboard</h1>

      <div style={styles.cards}>
        <div style={styles.card}>
          <h2>{threats}</h2>
          <p>Total Threats</p>
        </div>

        <div style={styles.card}>
          <h2>{criticalAlerts}</h2>
          <p>Critical Alerts</p>
        </div>

        <div style={styles.card}>
          <h2>92%</h2>
          <p>System Health</p>
        </div>
      </div>

      <ThreatGraph />
    </div>
  );
}

const styles = {
  main: {
    flex: 1,
    padding: "30px"
  },
  cards: {
    display: "flex",
    gap: "20px",
    marginTop: "30px"
  },
  card: {
    flex: 1,
    background: "#1e293b",
    padding: "25px",
    borderRadius: "12px",
    textAlign: "center"
  }
};

export default Dashboard;
