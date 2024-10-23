from flask import Flask, request, jsonify

@app.route('/api/filtrar_fornecedores', methods=['POST'])
def filtrar_fornecedores():
    data = request.get_json()
    consumo_mensal = data.get('consumo', 0)
    # lógica para buscar fornecedores com base no consumo mensal
    fornecedores = buscar_fornecedores_por_consumo_mensal(consumo_mensal)
    return jsonify(fornecedores)

def buscar_fornecedores_por_consumo_mensal(consumo_mensal):
    # Suponha que você tenha uma lista ou banco de dados de fornecedores
    fornecedores = Fornecedor.query.all()  # Exemplo de como pegar fornecedores do banco
    fornecedores_final = []
    for fornecedor in fornecedores:
        if float(consumo_mensal) >= fornecedor.limiteMinimoKwh:
            fornecedores_final.append(fornecedor)
    return fornecedores_final
