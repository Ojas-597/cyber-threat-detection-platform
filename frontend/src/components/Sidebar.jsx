import React from "react";

function Sidebar() {
  return (
    <div style={styles.sidebar}>
      <h2>🛡 SOC Panel</h2>

      <ul style={styles.menu}>
        <li>Dashboard</li>
        <li>Threats</li>
        <li>Incidents</li>
        <li>Packets</li>
        <li>Settings</li>
      </ul>
    </div>
  );
}

const styles = {
  sidebar: {
    width: "240px",
    background: "#111827",
    padding: "20px",
    minHeight: "100vh"
  },
  menu: {
    listStyle: "none",
    padding: 0,
    marginTop: "30px",
    lineHeight: "45px",
    fontSize: "18px"
  }
};

export default Sidebar;
