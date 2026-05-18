import React, { useState } from "react";

function ThreatIntel() {
  const [ip, setIp] = useState("");
  const [result, setResult] = useState(null);

  const checkIP = async () => {
    const token = localStorage.getItem("access_token");

    const res = await fetch(
      "http://127.0.0.1:8000/intel/ip",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ ip })
      }
    );

    const data = await res.json();
    setResult(data);
  };

  return (
    <div>
      <h1>Threat Intelligence</h1>

      <input
        value={ip}
        onChange={(e) => setIp(e.target.value)}
        placeholder="Enter IP address"
      />

      <button onClick={checkIP}>
        Check IP
      </button>

      {result && (
        <pre>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default ThreatIntel;