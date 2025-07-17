import React from 'react';
import { Link } from 'react-router-dom';
import './Perfil.css';
import logo from './Logo_FC_sem_fundo.png';

const Perfil = () => {
  const handleSubmit = (event) => {
    event.preventDefault();
    alert('Senha alterada com sucesso!');
    event.target.reset();
  };

  return (
    <div>
      <header className="navbar">
        <img src={logo} alt="Logo da Empresa" className="logo" />
        <nav>
          <Link to="/receituario" className="nav-button">Receituário</Link>
          <Link to="/romaneio" className="nav-button">Romaneio</Link>
          <Link to="/dashboard" className="nav-button">Dashboard</Link>
        </nav>
        <Link to="/perfil" className="nav-button user-profile-button">
          <div className="user-info">
            <span>Nome do Usuário</span>
            <span>email@example.com</span>
          </div>
        </Link>
      </header>
      <div className="profile-container">
        <h2>Alterar Senha</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="current-password">Senha Atual</label>
            <input type="password" id="current-password" name="current-password" />
          </div>
          <div className="input-group">
            <label htmlFor="new-password">Nova Senha</label>
            <input type="password" id="new-password" name="new-password" />
          </div>
          <div className="input-group">
            <label htmlFor="confirm-password">Confirmar Nova Senha</label>
            <input type="password" id="confirm-password" name="confirm-password" />
          </div>
          <button type="submit" className="save-button">Salvar</button>
        </form>
      </div>
    </div>
  );
};

export default Perfil;