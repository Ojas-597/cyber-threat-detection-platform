import React, { useEffect, useState } from "react";

function Packets() {
  const [packets, setPackets] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/packets/", {
      headers: {
        Authorization:
          "Bearer " + localStorage.getItem("access_token")
      }
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);

        if (data.packets) {
          setPackets(data.packets);
        } else if (Array.isArray(data)) {
          setPackets(data);
        } else {
          setPackets([]);
        }
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={styles.container}>
      <h1>Network Packet Monitoring</h1>

      {packets.length === 0 ? (
        <p>No packets found</p>
      ) : (
        packets.map((packet, index) => (
          <div key={index} style={styles.card}>
            <p>Source IP: {packet.source_ip}</p>
            <p>Destination IP: {packet.destination_ip}</p>
            <p>Protocol: {packet.protocol}</p>
            <p>Packet Size: {packet.packet_size}</p>
            <p>Risk Score: {packet.risk_score}</p>
            <p>Captured At: {packet.captured_at}</p>
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

export default Packets;