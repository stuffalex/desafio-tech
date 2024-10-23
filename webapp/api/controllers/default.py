from flask import Blueprint,jsonify
from model.tables import Fornecedor

default_bp = Blueprint('default', __name__)

@default_bp.route('/api/fornecedores', methods=['GET'])
def listar_fornecedores():
    fornecedores = Fornecedor.query.all()
    fornecedores_list = [
        {
            'id': fornecedor.id,
            'name': fornecedor.name,
            'custokwh': str(fornecedor.custokwh),
            'limiteMinimoKwh': str(fornecedor.limiteMinimoKwh),
            'ufOrigem': fornecedor.ufOrigem,
            'logo': fornecedor.logo
        }
        for fornecedor in fornecedores
    ]
    return jsonify(fornecedores_list)


@default_bp.route('/')
def home():
    return "hellou buddy"