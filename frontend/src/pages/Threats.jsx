import React, {
  useEffect,
  useState
} from "react";
import { useNavigate } from "react-router-dom";

function Threats() {
  const navigate = useNavigate();

  const [threats, setThreats] =
    useState([]);

  useEffect(() => {
    const token =
      localStorage.getItem(
        "access_token"
      );

    // Redirect if not logged in
    if (!token) {
      navigate("/");
      return;
    }

    fetch(
      "http://127.0.0.1:8000/threats/live",
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    )
      .then((res) => res.json())
      .then((data) => {
        setThreats(
          data.threats || []
        );
      })
      .catch((err) =>
        console.error(err)
      );
  }, [navigate]);

  return (
    <div style={styles.main}>
      <h1>Live Threats</h1>

      {threats.map((threat) => (
        <div
          key={threat.id}
          style={styles.card}
        >
          <h3>
            {threat.name}
          </h3>

          <p>
            Severity:{" "}
            {threat.severity}
          </p>

          <p>
            Status:{" "}
            {threat.status}
          </p>
        </div>
      ))}
    </div>
  );
}

const styles = {
  main: {
    flex: 1,
    padding: "30px"
  },

  card: {
    background: "#1e293b",
    padding: "20px",
    borderRadius: "10px",
    marginBottom: "15px"
  }
};

export default Threats;