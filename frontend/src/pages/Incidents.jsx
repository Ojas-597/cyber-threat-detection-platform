import React, { useEffect, useState } from "react";

function Incidents() {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/incidents/", {
      headers: {
        Authorization:
          "Bearer " + localStorage.getItem("access_token")
      }
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);

        // if backend returns { incidents: [...] }
        if (data.incidents) {
          setIncidents(data.incidents);
        }
        // if backend returns array directly
        else if (Array.isArray(data)) {
          setIncidents(data);
        }
        else {
          setIncidents([]);
        }
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={styles.container}>
      <h1>Incident Management</h1>

      {incidents.length === 0 ? (
        <p>No incidents found</p>
      ) : (
        incidents.map((incident, index) => (
          <div key={index} style={styles.card}>
            <p>
              ID: {incident.incident_id}
            </p>

            <p>
              Status: {incident.status}
            </p>

            <p>
              Response:
              {incident.response_action}
            </p>
          </div>
        ))
      )}
    </div>
  );
}

const styles = {
  container: {
    padding: "30px",
    color: "white"
  },

  card: {
    background: "#1e293b",
    padding: "20px",
    marginBottom: "15px",
    borderRadius: "8px"
  }
};

export default Incidents;