
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';
import logo from '../../Logo_FC_sem_fundo.png';

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');

    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();
        // You can save the token to localStorage if you plan to use it
        // localStorage.setItem('token', data.token);
        navigate('/perfil');
      } else {
        const errorData = await response.json();
        setError(errorData.message || 'Credenciais inválidas');
      }
    } catch (err) {
      setError('Falha ao conectar ao servidor. Tente novamente mais tarde.');
    }
  };

  return (
    <div className="login-container">
      <img src={logo} alt="Logo da Empresa" className="logo" />
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="username">Usuário</label>
          <input
            type="text"
            id="username"
            name="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="password">Senha</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p className="error-message">{error}</p>}
        <button type="submit" className="login-button">Entrar</button>
      </form>
    </div>
  );
};

export default Login;
