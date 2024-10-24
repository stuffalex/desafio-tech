import React, { useEffect, useState } from 'react';
import Navbar from './Barra';
import { Container, Button, Row, Col, Form, Table } from 'react-bootstrap';
import logo from './logo4.png';


    function Fornecedores() {
        const [fornecedores, setFornecedores] = useState([]);
        useEffect(() => {
          const fetchFornecedores = async () => {
            try {
              const response = await fetch('http://127.0.0.1:5000/api/fornecedores');
              if (!response.ok) {
                throw new Error('Erro ao carregar fornecedores');
              }
              const data = await response.json();
            console.log(data);

              setFornecedores(data);
            } catch (error) {
              console.error('Erro ao carregar fornecedores:', error);
            }
          };

          fetchFornecedores();
        }, []);

  return (
    <div>
    <Navbar/>
      <h1>Fornecedores</h1>
        <Row className="mt-3">
            <Col>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Logo</th>
                            <th>Nome fornecedor</th>
                            <th>Custo kWh</th>
                            <th>Limite Mínimo kWh</th>
                            <th>Numero de clientes</th>
                            <th>Nota média</th>
                            <th>UF de Origem</th>
                        </tr>
                    </thead>
                    <tbody>
                        {fornecedores.map((fornecedor) => (
                            <tr key={fornecedor.id}>
                                <td>
                                    <img src={logo} alt={`${fornecedor.nome} logo`} width="50" />
                                </td>
                                <td>{fornecedor.nome}</td>
                                <td>{fornecedor.custokwh}</td>
                                <td>{fornecedor.limiteMinimoKwh}</td>
                                <td>{fornecedor.numero_clientes}</td>
                                <td>{fornecedor.media_rating}</td>
                                 <td>{fornecedor.ufOrigem}</td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </Col>
        </Row>
    </div>
  );
}

export default Fornecedores;
