import React from "react";
import { Link, useNavigate } from "react-router-dom";

function Sidebar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    navigate("/");
    window.location.reload();
  };

  return (
    <div style={styles.sidebar}>
      <h2>🛡 SOC Panel</h2>

      <ul style={styles.menu}>
        <li>
          <Link to="/dashboard" style={styles.link}>
            Dashboard
          </Link>
        </li>

        <li>
          <Link to="/threats" style={styles.link}>
            Threats
          </Link>
        </li>

        <li>
          <Link to="/incidents" style={styles.link}>
            Incidents
          </Link>
        </li>

        <li>
          <Link to="/packets" style={styles.link}>
            Packets
          </Link>
        </li>

        <li>
          <Link to="/malware" style={styles.link}>
            Malware
          </Link>
        </li>

        <li>
          <Link to="/phishing" style={styles.link}>
            Phishing
          </Link>
        </li>

        <li>
          <Link to="/intrusion" style={styles.link}>
            Intrusion
          </Link>
        </li>

        <li>
          <Link to="/response" style={styles.link}>
            Response
          </Link>
        </li>
      </ul>

      <button
        onClick={handleLogout}
        style={styles.logoutBtn}
      >
        Logout
      </button>
    </div>
  );
}

const styles = {
  sidebar: {
    width: "240px",
    background: "#111827",
    padding: "20px",
    minHeight: "100vh",
    color: "white",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
  },

  menu: {
    listStyle: "none",
    padding: 0,
    marginTop: "30px",
    lineHeight: "45px",
    fontSize: "18px",
  },

  link: {
    color: "white",
    textDecoration: "none",
    display: "block",
  },

  logoutBtn: {
    padding: "12px",
    border: "none",
    borderRadius: "8px",
    background: "#ef4444",
    color: "white",
    fontWeight: "bold",
    cursor: "pointer",
    marginTop: "30px",
  },
};

export default Sidebar;