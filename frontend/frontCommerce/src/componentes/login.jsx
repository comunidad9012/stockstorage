import React, { useState } from "react";
import "../App.css";

function Login() {
  const [state, setState] = useState({
    email: "",
    password: "",
  });

  const inputChange = (e) => {
    const { name, value } = e.target;
    setState((prevState) => ({
      ...prevState,
      [name]: value, // Actualiza solo el campo que cambió
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const data = {
      email: state.email,
      password: state.password,
    };
    console.log(data);
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email</label>
        <input
          id="email"
          name="email"
          type="email"
          value={state.email} // Usar state en lugar de values
          onChange={inputChange}
        />
        <label htmlFor="password">Password</label>
        <input
          id="password"
          name="password"
          type="password"
          value={state.password} // Usar state en lugar de values
          onChange={inputChange}
        />
        <button type="submit">Sign Up</button>
      </form>
    </>
  );
}

export default Login;
