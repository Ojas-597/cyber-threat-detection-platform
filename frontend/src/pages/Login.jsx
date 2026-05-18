import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const [username, setUsername] =
    useState("");

  const [password, setPassword] =
    useState("");

  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/auth/login",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json"
          },
          body: JSON.stringify({
            username,
            password
          })
        }
      );

      const data =
        await response.json();

      console.log(data);

      if (data.access_token) {
        // Save JWT token
        localStorage.setItem(
          "access_token",
          data.access_token
        );

        // Go to dashboard
        navigate("/dashboard");
      } else {
        alert(
          data.detail ||
          "Login failed"
        );
      }

    } catch (err) {
      console.error(err);
      alert("Server error");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1>🛡 SOC Login</h1>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) =>
            setUsername(
              e.target.value
            )
          }
          style={styles.input}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
          style={styles.input}
        />

        <button
          onClick={handleLogin}
          style={styles.button}
        >
          Login
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    display: "flex",
    justifyContent:
      "center",
    alignItems:
      "center",
    background:
      "#0f172a"
  },

  card: {
    background:
      "#1e293b",
    padding: "40px",
    borderRadius:
      "12px",
    display: "flex",
    flexDirection:
      "column",
    gap: "20px",
    width: "320px",
    color: "white",
    boxShadow:
      "0 0 20px rgba(0,0,0,0.4)"
  },

  input: {
    padding: "12px",
    borderRadius:
      "8px",
    border: "none",
    fontSize: "16px"
  },

  button: {
    padding: "12px",
    border: "none",
    borderRadius:
      "8px",
    background:
      "#00ff99",
    color: "black",
    fontWeight:
      "bold",
    cursor: "pointer"
  }
};

export default Login;