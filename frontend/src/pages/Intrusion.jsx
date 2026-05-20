import React, { useState } from "react";

function Intrusion() {
  const [ip, setIp] = useState("");
  const [result, setResult] = useState(null);

  const checkIp = async () => {
    const token =
      localStorage.getItem(
        "access_token"
      );

    const response = await fetch(
      "http://127.0.0.1:8000/intrusion/check",
      {
        method: "POST",
        headers: {
          "Content-Type":
            "application/json",
          Authorization:
            `Bearer ${token}`
        },
        body: JSON.stringify({
          ip
        })
      }
    );

    const data =
      await response.json();

    setResult(data);
  };

  return (
    <div style={styles.main}>
      <h1>Intrusion Detection</h1>

      <input
        style={styles.input}
        value={ip}
        onChange={(e) =>
          setIp(e.target.value)
        }
        placeholder="Enter IP"
      />

      <button
        onClick={checkIp}
        style={styles.button}
      >
        Check IP
      </button>

      {result && (
        <pre style={styles.result}>
          {JSON.stringify(
            result,
            null,
            2
          )}
        </pre>
      )}
    </div>
  );
}

const styles = {
  main: {
    flex: 1,
    padding: "30px",
    color: "white"
  },
  input: {
    padding: "12px",
    width: "300px",
    marginRight: "10px"
  },
  button: {
    padding: "12px 20px",
    background: "#10b981",
    border: "none",
    color: "white"
  },
  result: {
    marginTop: "20px",
    background: "#1e293b",
    padding: "20px"
  }
};

export default Intrusion;