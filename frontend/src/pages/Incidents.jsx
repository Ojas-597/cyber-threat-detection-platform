import React, {
  useEffect,
  useState
} from "react";
import { useNavigate } from "react-router-dom";

function Incidents() {
  const navigate = useNavigate();

  const [incidents,
    setIncidents] =
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

    fetchIncidents();
  }, [navigate]);

  const fetchIncidents =
    async () => {
      try {
        const token =
          localStorage.getItem(
            "access_token"
          );

        const response =
          await fetch(
            "http://127.0.0.1:8000/incidents",
            {
              headers: {
                Authorization:
                  `Bearer ${token}`
              }
            }
          );

        const data =
          await response.json();

        console.log(
          "INCIDENTS DATA:",
          data
        );

        if (
          Array.isArray(
            data
          )
        ) {
          setIncidents(
            data
          );
        } else {
          setIncidents(
            []
          );
        }

      } catch (
        error
      ) {
        console.error(
          error
        );

        setIncidents(
          []
        );
      }
    };

  return (
    <div>
      <h1>
        Incidents
      </h1>

      {incidents.length ===
      0 ? (
        <p>
          No incidents
          found
        </p>
      ) : (
        incidents.map(
          (
            incident
          ) => (
            <div
              key={
                incident.id
              }
              style={{
                background:
                  "#1e293b",
                padding:
                  "15px",
                marginBottom:
                  "10px",
                borderRadius:
                  "8px"
              }}
            >
              <h3>
                {
                  incident.title
                }
              </h3>

              <p>
                Status:{" "}
                {
                  incident.status
                }
              </p>
            </div>
          )
        )
      )}
    </div>
  );
}

export default Incidents;