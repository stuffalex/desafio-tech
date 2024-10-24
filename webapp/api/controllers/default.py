from flask import Blueprint, jsonify, current_app
import logging

from model.tables import Cliente
from . import default_bp
from api import db

logging.basicConfig(level=logging.DEBUG)

@default_bp.route('/api/fornecedores', methods=['GET'])
def listar_fornecedores():
    from services.fornecedores_service import obter_fornecedores_com_info_de_clientes
    fornecedores_list= obter_fornecedores_com_info_de_clientes()
    # from model.tables import Fornecedor
    #
    # fornecedores_list = Fornecedor.query.all()
    return jsonify(fornecedores_list)

@default_bp.route('/api/popular_banco', methods=['POST'])
def popular_banco():
    try:
        fornecedores = []
        clientes = []
        clientes_fornecedores=[]
        print('oi')
        with open('C:/desafio/desafio-tech/webapp/api/controllers/clienteFornecedor.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                print('oie')
                dados = linha.strip().split(';')
                tipo = dados[0]
                print(dados[1], dados[2], dados[3])

                if tipo == "Fornecedor":
                    from model.tables import Fornecedor
                    print(dados[1], dados[2], dados[3], dados[4],dados[5])
                    fornecedor = Fornecedor(dados[1], dados[2], dados[3], dados[4],dados[5])
                    fornecedores.append(fornecedor)
                    db.session.add(fornecedor)

                elif tipo == "Cliente":
                    from model.tables import Cliente
                    cliente = Cliente(dados[1], dados[2], dados[3])
                    clientes.append(cliente)
                    db.session.add(cliente)

                elif tipo == "ClienteFornecedor":
                    from model.tables import ClienteFornecedor
                    cliente_fornecedor = ClienteFornecedor(dados[1], dados[2], dados[3])
                    clientes_fornecedores.append(cliente_fornecedor)
                    db.session.add(cliente_fornecedor)

        db.session.commit()

        print(fornecedores)
        print(clientes)
        print(clientes_fornecedores)
        return "sucess", 200
    except Exception as e:
        print(f"Error retrieving suppliers: {e}")
        return []

@default_bp.route('/api/fornecedores_por_consumo', methods=['POST'])
def listar_fornecedores_por_consumo_mensal(consumo_mensal):
    with current_app.app_context():
        from services.fornecedores_service import buscar_fornecedores_por_consumo_mensal
        fornecedores_filtrados = buscar_fornecedores_por_consumo_mensal(consumo_mensal)
        return jsonify(fornecedores_filtrados)

@default_bp.route('/')
def home():
    return "hellou buddy"


@default_bp.route('/api/get_cliente', methods=['GET'])
def get_cliente():
    lista = Cliente.query.all()

    clientes = [
        {
            "id": row.id,
            "nome": row.nome,
            "kwhMensal": row.kwhMensal,
            "ufOrigem": row.ufOrigem,
        }
        for row in lista
    ]
    return jsonify(clientes)
