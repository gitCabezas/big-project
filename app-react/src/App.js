import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import './App.css';
import Login from './Login';
import Perfil from './Perfil';
import Receituario from './Receituario';
import Romaneio from './Romaneio';
import Dashboard from './Dashboard';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/perfil" element={<Perfil />} />
          <Route path="/receituario" element={<Receituario />} />
          <Route path="/romaneio" element={<Romaneio />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
