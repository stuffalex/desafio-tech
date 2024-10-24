from api import db

from sqlalchemy import func
from model.tables import Fornecedor, ClienteFornecedor

def buscar_fornecedores_por_consumo_mensal(consumo_mensal):
    fornecedores = Fornecedor.query.all()
    fornecedores_final = []
    for fornecedor in fornecedores:
        if float(consumo_mensal) >= fornecedor.limiteMinimoKwh:
            fornecedores_final.append(fornecedor)
    return fornecedores_final

def obter_fornecedores_com_info_de_clientes():
    try:
        resultado = db.session.query(
            Fornecedor.id,
            Fornecedor.nome,
            Fornecedor.custoKwh,
            Fornecedor.limiteMinimoKwh,
            Fornecedor.ufOrigem,
            Fornecedor.logo,
            func.count(ClienteFornecedor.cliente_id).label('numero_clientes'),
            func.avg(ClienteFornecedor.rating).label('media_rating')
        ).outerjoin(ClienteFornecedor, Fornecedor.id == ClienteFornecedor.fornecedor_id) \
            .group_by(Fornecedor.id).all()

        fornecedores = [
            {
                "id": row.id,
                "nome": row.nome,
                "custokwh": f"{row.custoKwh:.2f}",
                "limiteMinimoKwh": f"{row.limiteMinimoKwh:.2f}",
                "ufOrigem": row.ufOrigem,
                "logo": row.logo,
                "numero_clientes": row.numero_clientes,
                "media_rating": f"{row.media_rating:.2f}"
            }
            for row in resultado
        ]
    except Exception as e:
        print(f"Error retrieving suppliers: {e}")
        return []

    return fornecedores