import React, { useState } from "react";

function Phishing() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkUrl = async () => {
    try {
      const token =
        localStorage.getItem(
          "access_token"
        );

      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/phishing/check",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
            Authorization:
              `Bearer ${token}`
          },
          body: JSON.stringify({
            url
          })
        }
      );

      const data =
        await response.json();

      setResult(data);
      setLoading(false);

    } catch (error) {
      console.error(error);
      setLoading(false);
    }
  };

  return (
    <div style={styles.main}>
      <h1>Phishing Detection</h1>

      <input
        style={styles.input}
        value={url}
        onChange={(e) =>
          setUrl(e.target.value)
        }
        placeholder="Enter URL"
      />

      <button
        onClick={checkUrl}
        style={styles.button}
      >
        Check URL
      </button>

      {loading && (
        <p>Checking...</p>
      )}

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

export default Phishing;