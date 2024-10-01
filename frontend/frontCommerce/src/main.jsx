import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
// import App from "./App.jsx";
import Login from "./componentes/login.jsx";
import SignUp from "./componentes/signUp.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Login />
    <SignUp />
  </StrictMode>
);
