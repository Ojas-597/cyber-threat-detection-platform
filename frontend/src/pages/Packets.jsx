import React, {
  useEffect,
  useState
} from "react";
import { useNavigate } from "react-router-dom";

function Packets() {
  const navigate = useNavigate();

  const [packets, setPackets] =
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

    fetchPackets();
  }, [navigate]);

  const fetchPackets = async () => {
    try {
      const token =
        localStorage.getItem(
          "access_token"
        );

      const response =
        await fetch(
          "http://127.0.0.1:8000/packets",
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
        "PACKETS:",
        data
      );

      if (Array.isArray(data)) {
        setPackets(data);
      } else if (
        data.packets &&
        Array.isArray(
          data.packets
        )
      ) {
        setPackets(
          data.packets
        );
      } else {
        setPackets([]);
      }

    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h1>Packets</h1>

      {packets.length === 0 ? (
        <p>No packets found</p>
      ) : (
        packets.map(
          (
            packet,
            index
          ) => (
            <div
              key={index}
              style={
                styles.card
              }
            >
              <h3>
                {
                  packet.source_ip
                }
                {" → "}
                {
                  packet.destination_ip
                }
              </h3>

              <p>
                Protocol:{" "}
                {
                  packet.protocol
                }
              </p>
            </div>
          )
        )
      )}
    </div>
  );
}

const styles = {
  card: {
    background:
      "#1e293b",
    padding: "20px",
    marginBottom: "15px",
    borderRadius:
      "10px",
    color: "white"
  }
};

export default Packets;