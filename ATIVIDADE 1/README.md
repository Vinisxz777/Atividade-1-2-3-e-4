# 🧮 Calculadora Inteligente (API Flask + Streamlit)

Este projeto é uma calculadora matemática completa dividida em três partes principais: uma **API Back-end** (construída com Flask), uma **Interface Visual Front-end** (construída com Streamlit) e um **Banco de Dados** local (SQLite) para armazenar o histórico de todas as operações realizadas.


## 🛠️ Pré-requisitos

pip install flask streamlit requests

## 🚀 Como Executar o Projeto

Como este projeto possui um Back-end e um Front-end que conversam entre si, você precisará abrir dois terminais diferentes na pasta raiz do projeto.

Passo 1: Ligar o Motor (A API Flask)
No Terminal 1, inicie o servidor rodando o arquivo principal:

python app.py

O terminal mostrará que o servidor está rodando no endereço http://127.0.0.1:5000. Deixe este terminal aberto para a API continuar funcionando!

Passo 2: Ligar a Tela (A Interface Streamlit)
Abra um Terminal 2 (uma nova aba ou janela), certifique-se de estar na mesma pasta do projeto, e rode:

streamlit run interface.py

## 📂 Estrutura do Projeto

Certifique-se de que os seus arquivos estejam organizados exatamente desta forma na sua pasta principal:

```text
seu_projeto/
│
├── app.py                  # Servidor Back-end (API Flask)
├── interface.py            # Interface Front-end (Streamlit)
├── README.md               # Documentação do projeto
│
└── banco_de_dados/         # Pasta do Banco de Dados
    ├── __init__.py         # Arquivo vazio (indica que é um pacote Python)
    ├── conexao.py          # Lógica de conexão com o SQLite
    └── historico.db        # Arquivo de banco criado automaticamente
