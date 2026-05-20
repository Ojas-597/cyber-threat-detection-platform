import React, {
  useEffect,
  useState
} from "react";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

function ThreatGraph({
  attackTrigger
}) {
  const [data, setData] = useState([
    { time: "1", attacks: 0 },
    { time: "2", attacks: 0 },
    { time: "3", attacks: 0 },
    { time: "4", attacks: 0 },
    { time: "5", attacks: 0 },
    { time: "6", attacks: 0 },
    { time: "7", attacks: 0 }
  ]);

  // Normal auto-refresh every 5 sec
  useEffect(() => {
    const token =
      localStorage.getItem(
        "access_token"
      );

    const headers = {
      Authorization:
        `Bearer ${token}`
    };

    const fetchThreatData = () => {
      fetch(
        "http://127.0.0.1:8000/threats/live",
        { headers }
      )
        .then((res) =>
          res.json()
        )
        .then((response) => {
          const threatCount =
            response.total_live_threats || 0;

          setData((prev) => {
            const updated = [
              ...prev
            ];

            updated.shift();

            updated.push({
              time:
                new Date()
                  .toLocaleTimeString(),
              attacks:
                threatCount
            });

            return updated;
          });
        })
        .catch((err) =>
          console.error(err)
        );
    };

    fetchThreatData();

    const interval =
      setInterval(
        fetchThreatData,
        5000
      );

    return () =>
      clearInterval(
        interval
      );

  }, []);

  // Simulate attack spike
  useEffect(() => {
    if (attackTrigger > 0) {
      setData((prev) =>
        prev.map(
          (item, index) =>
            index ===
            prev.length - 1
              ? {
                  ...item,
                  attacks:
                    item.attacks + 10
                }
              : item
        )
      );
    }
  }, [attackTrigger]);

  return (
    <div style={styles.container}>
      <h2>
        Weekly Threat Activity
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <LineChart data={data}>
          <CartesianGrid
            strokeDasharray="3 3"
          />

          <XAxis
            dataKey="time"
          />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="attacks"
            stroke="#00ff99"
            strokeWidth={3}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

const styles = {
  container: {
    marginTop: "40px",
    background: "#1e293b",
    padding: "20px",
    borderRadius: "12px"
  }
};

export default ThreatGraph;