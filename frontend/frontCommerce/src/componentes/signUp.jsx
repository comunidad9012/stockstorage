import React, { useState } from "react";
import "../App.css";

function SignUp() {
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

  const submit = (e) => {
    e.preventDefault();

    const data = {
      email: state.email,
      password: state.password,
    };
    console.log(data);

    fetch("127.0.0.1/usertest/signUp", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .catch((error) => console.error("error", error))
      .then((response) => console.log("exitoso", response));
  };

  return (
    <>
      <form onSubmit={submit} className="formulario">
        <h2>Registro de usuario</h2>
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

export default SignUp;
