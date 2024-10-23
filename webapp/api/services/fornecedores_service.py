import os
from model.tables import Fornecedor


def buscar_fornecedores_por_consumo_mensal(consumo_mensal):
    # Suponha que você tenha uma lista ou banco de dados de fornecedores
    fornecedores = Fornecedor.query.all()  # Exemplo de como pegar fornecedores do banco
    fornecedores_final = []
    for fornecedor in fornecedores:
        if float(consumo_mensal) >= fornecedor.limiteMinimoKwh:
            fornecedores_final.append(fornecedor)
    return fornecedores_final



def popular_fornecedores():
    file_path = os.path.join('app', 'data', 'fornecedores.txt')
    with open(file_path, 'r') as file:
        fornecedores = file.readlines()

    for fornecedor in fornecedores:
        name, custokwh, limiteMinimoKwh, ufOrigem, logo = fornecedor.strip().split(',')

        novo_fornecedor = Fornecedor(
            name=name,
            custoKwh=float(custokwh),
            limiteMinimoKwh=float(limiteMinimoKwh),
            ufOrigem=ufOrigem,
            logo=logo
        )

        db.session.add(novo_fornecedor)

    db.session.commit()
    return "Fornecedores populados com sucesso!"
