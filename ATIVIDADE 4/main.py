
import sqlite3
import pandas as pd

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    salario REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    funcionario_id INTEGER,
    FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id)
)
""")

# Limpar dados (evitar duplicação)
cursor.execute("DELETE FROM funcionarios")
cursor.execute("DELETE FROM livros")

# Inserir dados
funcionarios = [
    ("Ana", "Gerente", 3000),
    ("Bruno", "Assistente", 2000),
    ("Carlos", "Bibliotecario", 2500)
]

cursor.executemany("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", funcionarios)

# Criar CSV de livros
df_livros = pd.DataFrame({
    "titulo": ["Python Basico", "Banco de Dados", "Data Science"],
    "autor": ["Joao Silva", "Maria Souza", "Pedro Lima"],
    "ano": [2020, 2019, 2021],
    "funcionario_id": [1, 2, 3]
})

df_livros.to_csv("livros.csv", index=False)

# Ler CSV e inserir
df_csv = pd.read_csv("livros.csv")
df_csv.to_sql("livros", conn, if_exists="append", index=False)

# UPDATE (aumentar salário)
cursor.execute("UPDATE funcionarios SET salario = salario * 1.1")

# DELETE (remover livros antigos)
cursor.execute("DELETE FROM livros WHERE ano < 2020")

conn.commit()

# JOIN
query = """
SELECT f.nome, f.cargo, f.salario, l.titulo, l.autor
FROM funcionarios f
JOIN livros l ON f.id = l.funcionario_id
"""

df = pd.read_sql_query(query, conn)

# Análises
media_salario = df["salario"].mean()
contagem = df.groupby("cargo").count()

print("Media Salarial:", media_salario)
print("\nContagem por Cargo:")
print(contagem)

# Exportar Excel
with pd.ExcelWriter("resultado.xlsx") as writer:
    df.to_excel(writer, sheet_name="Dados", index=False)
    contagem.to_excel(writer, sheet_name="Resumo")

conn.close()
