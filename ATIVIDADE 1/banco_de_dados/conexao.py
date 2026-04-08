import sqlite3
import os

PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BD = os.path.join(PASTA_ATUAL, 'historico.db')

def conectar():
    """Abre a conexão com o banco de dados."""
    return sqlite3.connect(CAMINHO_BD)

def criar_tabela():
    """Cria a tabela no banco caso ela ainda não exista."""
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS operacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor_a REAL,
            valor_b REAL,
            operacao TEXT,
            resultado REAL
        )
    ''')
    
    conn.commit() 
    conn.close() 

def salvar_operacao(a, b, operacao, resultado):
    """Insere os dados de uma nova conta no banco."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO operacoes (valor_a, valor_b, operacao, resultado)
        VALUES (?, ?, ?, ?)
    ''', (a, b, operacao, resultado))
    
    conn.commit()
    conn.close()