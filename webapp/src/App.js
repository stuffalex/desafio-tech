
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
//import Fornecedores from './Fornecedores';
//import FornecedoresFiltrados from './FornecedoresFiltrados';

function App() {


  return (
  <div><p>OLÁ</p></div>
    <Router>
      <Routes>
        <Route path="/"><Home /> </Route>
//        <Route path="/fornecedores"><Fornecedores/></Route>
//        <Route path="/fornecedoresFiltrados"><FornecedoresFiltrados /></Route>
      </Routes>
    </Router>
  );
}

export default App;

