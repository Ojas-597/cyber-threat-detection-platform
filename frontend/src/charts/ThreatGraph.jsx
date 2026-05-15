import React from "react";

import {

  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer

} from "recharts";

const data = [

  {
    time: "10AM",
    attacks: 4
  },

  {
    time: "11AM",
    attacks: 12
  },

  {
    time: "12PM",
    attacks: 7
  },

  {
    time: "1PM",
    attacks: 18
  },

  {
    time: "2PM",
    attacks: 9
  },

  {
    time: "3PM",
    attacks: 14
  }
];

function ThreatGraph() {

  return (

    <div
      style={{
        backgroundColor: "white",
        padding: "20px",
        borderRadius: "10px",
        boxShadow: "0px 2px 10px rgba(0,0,0,0.1)"
      }}
    >

      <h2 style={{ marginBottom: "20px" }}>
        Real-Time Threat Activity
      </h2>

      <ResponsiveContainer width="100%" height={350}>

        <LineChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="time" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="attacks"
            strokeWidth={3}
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  );
}

export default ThreatGraph;
