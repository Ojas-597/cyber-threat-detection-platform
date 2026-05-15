import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

const data = [
  { day: "Mon", threats: 12 },
  { day: "Tue", threats: 18 },
  { day: "Wed", threats: 9 },
  { day: "Thu", threats: 24 },
  { day: "Fri", threats: 15 },
  { day: "Sat", threats: 30 },
  { day: "Sun", threats: 20 }
];

function App() {
  return (
    <div style={styles.container}>
      
      <div style={styles.sidebar}>
        <h2>🛡 SOC Panel</h2>

        <ul style={styles.menu}>
          <li>Dashboard</li>
          <li>Threats</li>
          <li>Incidents</li>
          <li>Reports</li>
          <li>Settings</li>
        </ul>
      </div>

      <div style={styles.main}>

        <h1>Cyber Threat Detection Dashboard</h1>

        <div style={styles.cards}>

          <div style={styles.card}>
            <h2>128</h2>
            <p>Total Threats</p>
          </div>

          <div style={styles.card}>
            <h2>18</h2>
            <p>Critical Alerts</p>
          </div>

          <div style={styles.card}>
            <h2>92%</h2>
            <p>System Health</p>
          </div>

        </div>

        <div style={styles.chartContainer}>
          <h2>Weekly Threat Activity</h2>

          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="day" />
              <YAxis />
              <Tooltip />
              <Line
                type="monotone"
                dataKey="threats"
                stroke="#00ff99"
                strokeWidth={3}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>

      </div>
    </div>
  );
}

const styles = {

  container: {
    display: "flex",
    minHeight: "100vh",
    background: "#0f172a"
  },

  sidebar: {
    width: "250px",
    background: "#111827",
    padding: "20px"
  },

  menu: {
    listStyle: "none",
    marginTop: "30px",
    lineHeight: "50px",
    fontSize: "18px"
  },

  main: {
    flex: 1,
    padding: "30px"
  },

  cards: {
    display: "flex",
    gap: "20px",
    marginTop: "30px"
  },

  card: {
    flex: 1,
    background: "#1e293b",
    padding: "25px",
    borderRadius: "12px",
    textAlign: "center"
  },

  chartContainer: {
    marginTop: "40px",
    background: "#1e293b",
    padding: "20px",
    borderRadius: "12px"
  }
};

export default App;
