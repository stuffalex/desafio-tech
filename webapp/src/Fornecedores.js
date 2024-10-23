import React, { useEffect, useState } from 'react';
import Navbar from './Barra';

function Fornecedores() {
  const [fornecedores, setFornecedores] = useState([]);

  useEffect(() => {
    fetch('/api/fornecedores')
      .then((response) => response.json())
      .then((data) => setFornecedores(data))
      .catch((error) => console.error('Erro ao carregar fornecedores:', error));
  }, []);

  return (
    <div>
    <Navbar/>
      <h1>Fornecedores</h1>
      <ul>
        {fornecedores.map((fornecedor) => (
          <li key={fornecedor.id}>
            <img src={fornecedor.logo} alt={`${fornecedor.name} logo`} width="50" />
            <p>Nome: {fornecedor.name}</p>
            <p>Custo kWh: {fornecedor.custokwh}</p>
            <p>Limite Mínimo kWh: {fornecedor.limiteMinimoKwh}</p>
            <p>UF de Origem: {fornecedor.ufOrigem}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Fornecedores;
