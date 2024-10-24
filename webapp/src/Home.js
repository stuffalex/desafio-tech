import React, { useState } from 'react';
import { Container, Button, Row, Col, Form } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import Navbar from './Barra';

function Home() {
    const [consumo, setConsumo] = useState('');
    const navigate = useNavigate();

    const handleInputChange = (e) => {
        setConsumo(e.target.value);
    };

    const handleCalcular = async () => {
        try {
            const response = await fetch('https://desafio-tech-back.vercel.app/api/fornecedores_por_consumo', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ consumo_mensal: consumo }),
            });

            if (!response.ok) {
                throw new Error('Erro ao calcular fornecedores');
            }

            const data = await response.json();
            navigate('/fornecedoresFiltrados', { state: { consumo: data } });
        } catch (error) {
            console.error('Erro ao calcular:', error);
        }
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            handleCalcular();
        }
    };

    return (
        <div>
            <Navbar/>
            <Container className="mt-5">
                <Row>
                    <Col md={6}>
                        <h2>Bem-vindo ao nosso site</h2>
                        <Button variant="primary" onClick={() => navigate('/fornecedores')}>
                          Ver Fornecedores
                        </Button>
                    </Col>
                </Row>
                <Row>
                    <Form>
                        <Form.Group className="mb-3" controlId="formLogin">
                            <Form.Label>Consumo mensal em Kwh</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="Ex: 150kWh"
                                value={consumo}
                                onChange={handleInputChange}
                                onKeyDown={handleKeyDown}
                            />
                            </Form.Group>
                        <Button variant="primary" onClick={handleCalcular}>
                            Calcular Fornecedores
                        </Button>
                    </Form>
                </Row>
            </Container>
        </div>
    );
}

export default Home;
