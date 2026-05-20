import React, { useState } from "react";

function Response() {
  const [ip, setIp] = useState("");
  const [result, setResult] = useState(null);

  const blockIp = async () => {
    const token =
      localStorage.getItem(
        "access_token"
      );

    const response = await fetch(
      "http://127.0.0.1:8000/response/block",
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
      <h1>Incident Response</h1>

      <input
        style={styles.input}
        value={ip}
        onChange={(e) =>
          setIp(e.target.value)
        }
        placeholder="Enter IP to block"
      />

      <button
        onClick={blockIp}
        style={styles.button}
      >
        Block IP
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
    background: "#ef4444",
    border: "none",
    color: "white"
  },
  result: {
    marginTop: "20px",
    background: "#1e293b",
    padding: "20px"
  }
};

export default Response;