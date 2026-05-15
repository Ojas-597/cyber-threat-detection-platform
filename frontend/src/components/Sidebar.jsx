import React from "react";

function Sidebar() {

  return (

    <div
      style={{
        width: "250px",
        height: "100vh",
        backgroundColor: "#111827",
        color: "white",
        padding: "20px",
        position: "fixed"
      }}
    >

      <h2 style={{ marginBottom: "30px" }}>
        Cyber SOC
      </h2>

      <ul style={{ listStyle: "none", padding: 0 }}>

        <li style={menuStyle}>
          Dashboard
        </li>

        <li style={menuStyle}>
          Threat Monitoring
        </li>

        <li style={menuStyle}>
          Incident Response
        </li>

        <li style={menuStyle}>
          Threat Intelligence
        </li>

        <li style={menuStyle}>
          MITRE ATT&CK
        </li>

        <li style={menuStyle}>
          CVE Feed
        </li>

        <li style={menuStyle}>
          Malware Scanner
        </li>

        <li style={menuStyle}>
          Settings
        </li>

      </ul>

    </div>
  );
}

const menuStyle = {

  padding: "12px",
  marginBottom: "10px",
  backgroundColor: "#1F2937",
  borderRadius: "8px",
  cursor: "pointer"
};

export default Sidebar;
