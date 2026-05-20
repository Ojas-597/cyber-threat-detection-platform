import React from "react";
import {
  Routes,
  Route
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Threats from "./pages/Threats";
import Incidents from "./pages/Incidents";
import Packets from "./pages/Packets";
import Malware from "./pages/Malware";
import Phishing from "./pages/Phishing";
import Intrusion from "./pages/Intrusion";
import Response from "./pages/Response";

import Sidebar from "./components/Sidebar";
import ProtectedRoute from "./components/ProtectedRoute";

function ProtectedLayout({ children }) {
  return (
    <div style={styles.app}>
      <Sidebar />
      {children}
    </div>
  );
}

function App() {
  return (
    <Routes>
      {/* Login page */}
      <Route
        path="/"
        element={<Login />}
      />

      {/* Dashboard */}
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Dashboard />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />

      {/* Threats */}
      <Route
        path="/threats"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Threats />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />

      {/* Incidents */}
      <Route
        path="/incidents"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Incidents />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />

      {/* Packets */}
      <Route
        path="/packets"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Packets />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />

      {/* Malware */}
      <Route
        path="/malware"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Malware />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />

      {/* Phishing */}
      <Route
        path="/phishing"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Phishing />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />

      {/* Intrusion */}
      <Route
        path="/intrusion"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Intrusion />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />

      {/* Incident Response */}
      <Route
        path="/response"
        element={
          <ProtectedRoute>
            <ProtectedLayout>
              <Response />
            </ProtectedLayout>
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}

const styles = {
  app: {
    display: "flex",
    minHeight: "100vh",
    background: "#0f172a",
    color: "white"
  }
};

export default App;