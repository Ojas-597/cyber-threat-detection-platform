import { useEffect, useState } from "react";

function Dashboard() {

  const [threats, setThreats] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/threats/live")

      .then(response => response.json())

      .then(data => {

        setThreats(data.threats);
      });

  }, []);

  return (

    <div style={{ padding: "20px" }}>

      <h1>Cyber Threat Dashboard</h1>

      <table border="1" cellPadding="10">

        <thead>

          <tr>
            <th>Type</th>
            <th>Severity</th>
            <th>Status</th>
          </tr>

        </thead>

        <tbody>

          {threats.map((threat, index) => (

            <tr key={index}>

              <td>{threat.type}</td>
              <td>{threat.severity}</td>
              <td>{threat.status}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Dashboard;
