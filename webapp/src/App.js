
import React from 'react';
import { Routes, Router, Route } from 'react-router-dom';
import Home from './Home';
import Fornecedores from './Fornecedores';
import FornecedoresFiltrados from './FornecedoresFiltrados';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/fornecedores" element={<Fornecedores />} />
        <Route path="/fornecedoresFiltrados" element={<FornecedoresFiltrados />} />
      </Routes>
    </Router>
  );
}

export default App;
