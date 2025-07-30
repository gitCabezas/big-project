import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';
import logo from '../../../Logo_FC_sem_fundo.png';

const Navbar = () => {
  const location = useLocation();

  return (
    <header className="navbar">
      <img src={logo} alt="Logo da Empresa" className="logo" />
      <nav>
        <Link to="/receituario" className={`nav-button ${location.pathname === '/receituario' ? 'active' : ''}`}>
          Receituário
        </Link>
        <Link to="/romaneio" className={`nav-button ${location.pathname === '/romaneio' ? 'active' : ''}`}>
          Romaneio
        </Link>
        
      </nav>
      <Link to="/perfil" className={`nav-button user-profile-button ${location.pathname === '/perfil' ? 'active' : ''}`}>
        <div className="user-info">
          <span>Nome do Usuário</span>
          <span>email@example.com</span>
        </div>
      </Link>
    </header>
  );
};

export default Navbar;