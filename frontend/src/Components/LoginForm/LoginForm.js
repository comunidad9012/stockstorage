import React from 'react'
import './LoginForm.css';

export const LoginForm = () => {
  return (
    <div className='wrapper'>
      <form action="">
        <h1>Login</h1>
        <div className='input-box'>
          <input type="text" placeholder='Nombre'requered/>
        </div>
        <div className='input-box'>
          <input type="contraseña" placeholder='Contraseña'requered/>
        </div>
        <div className='Olvide-mi-contraseña'>
          <label><input type="checkbox"/>Recordar nombre de usuario</label>
          <a href='#'>¿Olvidaste tu contraseña?</a>
        </div>

        <button type="submit">Iniciar sesión</button>
        <div className='register-link'>
          <p>¿No tienes cuenta? Regístrate aquí <a href="#">Registrarse </a></p>
        </div>

      </form>

    </div>
  )
}
