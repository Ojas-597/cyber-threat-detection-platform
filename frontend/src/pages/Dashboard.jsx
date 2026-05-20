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

  const [liveThreats, setLiveThreats] =
    useState(0);

  const [attackTrigger,
    setAttackTrigger] =
    useState(0);

  // MITRE ATT&CK
  const [mitreTechnique,
    setMitreTechnique] =
    useState(
      "T1566 - Phishing"
    );

  // Threat Intelligence IOC
  const [threatIntel,
    setThreatIntel] =
    useState(
      "185.220.101.1"
    );

  useEffect(() => {
    const token =
      localStorage.getItem(
        "access_token"
      );

    if (!token) {
      navigate("/");
      return;
    }

    const headers = {
      Authorization:
        `Bearer ${token}`
    };

    const fetchDashboardData =
      () => {

      // Threat summary
      fetch(
        "http://127.0.0.1:8000/threats/analytics/summary",
        { headers }
      )
        .then((res) =>
          res.json()
        )
        .then((data) => {
          setSummary(data);
        })
        .catch((err) =>
          console.error(err)
        );

      // Live threats
      fetch(
        "http://127.0.0.1:8000/threats/live",
        { headers }
      )
        .then((res) =>
          res.json()
        )
        .then((data) => {
          setLiveThreats(
            data.total_live_threats
          );
        })
        .catch((err) =>
          console.error(err)
        );

      // Threat Intelligence IOC
      fetch(
        "http://127.0.0.1:8000/intel/iocs",
        { headers }
      )
        .then((res) =>
          res.json()
        )
        .then((data) => {
          if (
            data.malicious_ips &&
            data.malicious_ips.length > 0
          ) {
            setThreatIntel(
              data.malicious_ips[0]
            );
          }
        })
        .catch((err) =>
          console.error(err)
        );
    };

    // Initial load
    fetchDashboardData();

    // Auto refresh every 5 sec
    const interval =
      setInterval(
        fetchDashboardData,
        5000
      );

    return () =>
      clearInterval(
        interval
      );

  }, [navigate]);

  // Simulate attack
  const simulateAttack =
    () => {

      // Increase threat counts
      setLiveThreats(
        (prev) => prev + 1
      );

      setSummary(
        (prev) => ({
          ...prev,
          critical:
            prev.critical + 1,
          high:
            prev.high + 1
        })
      );

      // Rotate MITRE ATT&CK
      const mitreTechniques = [
        "T1498 - Network Denial of Service",
        "T1190 - Exploit Public-Facing Application",
        "T1566 - Phishing",
        "T1204 - User Execution"
      ];

      setMitreTechnique(
        mitreTechniques[
          Math.floor(
            Math.random() *
            mitreTechniques.length
          )
        ]
      );

      // Rotate IOC
      const iocs = [
        "185.220.101.1",
        "8.8.8.8",
        "1.2.3.4",
        "bad-domain.example"
      ];

      setThreatIntel(
        iocs[
          Math.floor(
            Math.random() *
            iocs.length
          )
        ]
      );

      // Trigger graph spike
      setAttackTrigger(
        (prev) => prev + 1
      );
    };

  return (
    <div style={styles.main}>
      <h1>
        Cyber Threat Dashboard
      </h1>

      <button
        style={styles.button}
        onClick={
          simulateAttack
        }
      >
        Simulate Attack
      </button>

      {/* Main cards */}
      <div style={styles.cards}>
        <Card
          label="Live Threats"
          value={
            liveThreats
          }
        />

        <Card
          label="Critical"
          value={
            summary.critical
          }
        />

        <Card
          label="High"
          value={
            summary.high
          }
        />

        <Card
          label="Medium"
          value={
            summary.medium
          }
        />
      </div>

      {/* MITRE + Intel */}
      <div style={styles.cards}>
        <Card
          label="MITRE ATT&CK"
          value={
            mitreTechnique
          }
        />

        <Card
          label="Threat Intel IOC"
          value={
            threatIntel
          }
        />
      </div>

      {/* Graph */}
      <ThreatGraph
        attackTrigger={
          attackTrigger
        }
      />
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

  button: {
    marginTop: "20px",
    padding:
      "12px 20px",
    border: "none",
    borderRadius: "8px",
    background:
      "#ef4444",
    color: "white",
    fontWeight:
      "bold",
    cursor: "pointer"
  },

  cards: {
    display: "flex",
    gap: "20px",
    marginTop: "20px"
  },

  card: {
    flex: 1,
    background:
      "#1e293b",
    padding: "20px",
    borderRadius:
      "12px",
    textAlign:
      "center"
  }
};

export default Dashboard;