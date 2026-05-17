import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

const data = [
  { day: "Mon", attacks: 12 },
  { day: "Tue", attacks: 18 },
  { day: "Wed", attacks: 9 },
  { day: "Thu", attacks: 24 },
  { day: "Fri", attacks: 15 },
  { day: "Sat", attacks: 30 },
  { day: "Sun", attacks: 20 }
];

function ThreatGraph() {
  return (
    <div style={styles.container}>
      <h2>Weekly Threat Activity</h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <LineChart data={data}>
          <CartesianGrid
            strokeDasharray="3 3"
          />
          <XAxis dataKey="day" />
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
