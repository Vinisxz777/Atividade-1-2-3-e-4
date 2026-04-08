import streamlit as st
import requests

st.title("Calculadora Inteligente")

operacao = st.selectbox(
    "Escolha a operação matemática:",
    (
        "soma", "subtracao", "multiplicacao", "divisao", 
        "raiz_quadrada", "raiz_cubica", "elevacao_quadrado", "elevacao_cubo"
    )
)

operacoes_simples = ["raiz_quadrada", "raiz_cubica", "elevacao_quadrado", "elevacao_cubo"]

col1, col2 = st.columns(2)

with col1:
    valor_a_str = st.text_input("Digite o valor (A):", value="", placeholder="Ex: 10")

with col2:
    if operacao not in operacoes_simples:
        valor_b_str = st.text_input("Digite o valor (B):", value="", placeholder="Ex: 5")
    else:
        valor_b_str = None

if st.button("Calcular"):
    
    try:
        valor_a = float(valor_a_str.replace(",", "."))
        
        if valor_b_str is not None:
            valor_b = float(valor_b_str.replace(",", "."))
        else:
            valor_b = None
            
        dados_para_api = {
            "a": valor_a,
            "b": valor_b,
            "operacao": operacao
        }
        
        url_da_api = "http://127.0.0.1:5000/calcular"
        
        resposta = requests.post(url_da_api, json=dados_para_api)
        dados_resposta = resposta.json()
        
        if resposta.status_code == 200:
            st.success(f"O resultado é: **{dados_resposta['resultado']}**")
            st.info(dados_resposta['mensagem'])
        else:
            st.error(f"Erro na API: {dados_resposta.get('erro')}")
            
    except ValueError:
        st.warning("Por favor, digite apenas números válidos nos campos antes de calcular.")
        
    except requests.exceptions.ConnectionError:
        st.error("Não foi possível conectar a API.")