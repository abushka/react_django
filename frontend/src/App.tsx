import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Chat } from "./components/Chat";
import { Login } from "./components/Login";
import { Navbar } from "./components/Navbar";
import { AuthContextProvider } from "./contexts/AuthContext";
import { ProtectedRoute } from "./components/ProtectedRoute"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <AuthContextProvider>
              <Navbar />
            </AuthContextProvider>
          }
        >
          <Route
            path=""
            element={
              <ProtectedRoute>
                {/* <Conversations /> */}
              </ProtectedRoute>
            }
          />
          <Route
            path="chats/:conversationName"
            element={
              <ProtectedRoute>
                <Chat />
              </ProtectedRoute>
            }
          />
          <Route path="login" element={<Login />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}