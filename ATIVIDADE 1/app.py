from flask import Flask, request, jsonify
import math
from banco_de_dados.conexao import criar_tabela, salvar_operacao

app = Flask(__name__)
criar_tabela()

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json(silent=True)
    
    if not dados:
        return jsonify({"erro": "O corpo da requisição deve ser um JSON válido."}), 400

    a = dados.get("a")
    b = dados.get("b")
    operacao = dados.get("operacao")

    operacoes_simples = ["raiz_quadrada", "raiz_cubica", "elevacao_quadrado", "elevacao_cubo"]
    operacoes_duplas = ["soma", "subtracao", "multiplicacao", "divisao"]

    if a is None or operacao is None:
        return jsonify({"erro": "Faltam parâmetros 'a' ou 'operacao'."}), 400

    if operacao in operacoes_duplas and b is None:
        return jsonify({"erro": "O parâmetro 'b' é obrigatório para esta operação."}), 400

    if operacao == "soma":
        resultado = a + b
    elif operacao == "subtracao":
        resultado = a - b
    elif operacao == "multiplicacao":
        resultado = a * b
    elif operacao == "divisao":
        if b == 0:
            return jsonify({"erro": "Não é possível fazer divisão por zero."}), 400
        resultado = a / b
        
    elif operacao == "raiz_quadrada":
        if a < 0:
            return jsonify({"erro": "Não é possível calcular raiz quadrada de número negativo aqui."}), 400
        resultado = math.sqrt(a)
    elif operacao == "raiz_cubica":
        resultado = a ** (1/3) if a >= 0 else -((-a) ** (1/3))
    elif operacao == "elevacao_quadrado":
        resultado = a ** 2
    elif operacao == "elevacao_cubo":
        resultado = a ** 3
    else:
        return jsonify({"erro": "Operação inválida."}), 400
    
    salvar_operacao(a, b, operacao, resultado)

    return jsonify({
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": resultado,
        "mensagem": "Cálculo salvo no banco de dados!"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)