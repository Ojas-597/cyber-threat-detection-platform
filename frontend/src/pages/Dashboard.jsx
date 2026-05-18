import React, {
  useEffect,
  useState
} from "react";

import { useNavigate } from "react-router-dom";
import ThreatGraph from "../charts/ThreatGraph";

function Dashboard() {
  const navigate = useNavigate();

  const [summary, setSummary] = useState({
    critical: 0,
    high: 0,
    medium: 0,
    low: 0
  });

  const [liveThreats, setLiveThreats] = useState(0);

  useEffect(() => {
    const token = localStorage.getItem(
      "access_token"
    );

    // Redirect to login if no token
    if (!token) {
      navigate("/");
      return;
    }

    const headers = {
      Authorization: `Bearer ${token}`
    };

    fetch(
      "http://127.0.0.1:8000/threats/analytics/summary",
      { headers }
    )
      .then((res) => res.json())
      .then((data) => {
        setSummary(data);
      });

    fetch(
      "http://127.0.0.1:8000/threats/live",
      { headers }
    )
      .then((res) => res.json())
      .then((data) => {
        setLiveThreats(
          data.total_live_threats
        );
      });
  }, [navigate]);

  return (
    <div style={styles.main}>
      <h1>Cyber Threat Dashboard</h1>

      <div style={styles.cards}>
        <Card
          label="Live Threats"
          value={liveThreats}
        />
        <Card
          label="Critical"
          value={summary.critical}
        />
        <Card
          label="High"
          value={summary.high}
        />
        <Card
          label="Medium"
          value={summary.medium}
        />
      </div>

      <ThreatGraph />
    </div>
  );
}

function Card({
  label,
  value
}) {
  return (
    <div style={styles.card}>
      <h2>{value}</h2>
      <p>{label}</p>
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
    marginTop: "20px"
  },

  card: {
    flex: 1,
    background: "#1e293b",
    padding: "20px",
    borderRadius: "12px",
    textAlign: "center"
  }
};

export default Dashboard;