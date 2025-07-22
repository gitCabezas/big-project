import React from 'react';
import Navbar from '../../common/components/Navbar/Navbar';

const Perfil = () => {
  const handleSubmit = (event) => {
    event.preventDefault();
    alert('Senha alterada com sucesso!');
    event.target.reset();
  };

  return (
    <div>
      <Navbar />
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