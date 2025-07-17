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

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/perfil" element={<Perfil />} />
          <Route path="/receituario" element={<Receituario />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
