
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';
import logo from './Logo_FC_sem_fundo.png';

const Login = () => {
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    navigate('/perfil');
  };

  return (
    <div className="login-container">
      <img src={logo} alt="Logo da Empresa" className="logo" />
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="username">Usuário</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div className="input-group">
          <label htmlFor="password">Senha</label>
          <input type="password" id="password" name="password" required />
        </div>
        <button type="submit" className="login-button">Entrar</button>
      </form>
    </div>
  );
};

export default Login;
