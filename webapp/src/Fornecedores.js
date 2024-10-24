//import React, { useEffect, useState } from 'react';
//import Navbar from './Barra';
//
//    function Fornecedores() {
//        const [fornecedores, setFornecedores] = useState([]);
//        useEffect(() => {
//          const fetchFornecedores = async () => {
//            try {
//              const response = await fetch('/api/fornecedores');
//              if (!response.ok) {
//                throw new Error('Erro ao carregar fornecedores');
//              }
//              const data = await response.json();
//              setFornecedores(data);
//            } catch (error) {
//              console.error('Erro ao carregar fornecedores:', error);
//            }
//          };
//
//          fetchFornecedores();
//        }, []);
//
//  return (
//    <div>
//    <Navbar/>
//      <h1>Fornecedores</h1>
//      <ul>
//        {fornecedores.map((fornecedor) => (
//          <li key={fornecedor.id}>
//            <img src={fornecedor.logo} alt={`${fornecedor.name} logo`} width="50" />
//            <p>Nome: {fornecedor.name}</p>
//            <p>Custo kWh: {fornecedor.custoKwh}</p>
//            <p>Limite Mínimo kWh: {fornecedor.limiteMinimoKwh}</p>
//            <p>UF de Origem: {fornecedor.ufOrigem}</p>
//          </li>
//        ))}
//      </ul>
//    </div>
//  );
//}
//
//export default Fornecedores;
