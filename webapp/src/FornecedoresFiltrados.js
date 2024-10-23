import React, { useState } from 'react';
import { Container, Button, Row, Col, Form, Table } from 'react-bootstrap';
import { useLocation } from 'react-router-dom';
import Navbar from './Barra';
import logo from './logo4.png';

function FornecedoresFiltrados() {
    const [fornecedores, setFornecedores] = useState(null);
    const location = useLocation();
    const [consumoLocal, setConsumoLocal] = useState(location.state?.consumo || '');

    const handleInputChange = (e) => {
        setConsumoLocal(e.target.value);
    };

    const handleCalcular = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/filtrar_fornecedores', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ consumo: consumoLocal }),
            });

            if (!response.ok) {
                throw new Error('Erro ao calcular fornecedores');
            }

            const data = await response.json();
            setFornecedores(data);
        } catch (error) {
            console.error('Erro ao calcular:', error);
        }
    };

    return (
        <div>
            <Navbar />
            <Container className="mt-5">
                <Row>
                    <Form>
                        <Form.Group className="mb-3" controlId="formConsumo">
                            <Form.Label>Consumo mensal em Kwh</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="Ex: 150kWh"
                                value={consumoLocal}
                                onChange={handleInputChange}
                            />
                        </Form.Group>
                        <Button variant="primary" onClick={handleCalcular}>
                            Calcular Fornecedores
                        </Button>
                    </Form>
                </Row>

                {fornecedores && (
                    <Row className="mt-3">
                        <Col>
                            <h3>Fornecedores:</h3>
                            <Table striped bordered hover>
                                <thead>
                                    <tr>
                                        <th>Logo</th>
                                        <th>Nome fornecedor</th>
                                        <th>Custo kWh</th>
                                        <th>Limite Mínimo kWh</th>
                                        <th>UF de Origem</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {fornecedores.map((fornecedor) => (
                                        <tr key={fornecedor.id}>
                                            <td>
                                                <img src={logo} alt={`${fornecedor.name} logo`} width="50" />
                                            </td>
                                            <td>{fornecedor.name}</td>
                                            <td>{fornecedor.custokwh}</td>
                                            <td>{fornecedor.limiteMinimoKwh}</td>
                                            <td>{fornecedor.ufOrigem}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </Table>
                        </Col>
                    </Row>
                )}
            </Container>
        </div>
    );
}

export default FornecedoresFiltrados;
