import pandas as pd

df = pd.read_csv('clientes.csv')

# Verifica os primeiros registros
print(df.head().to_string())

# Verifica a quantidade de linhas e colunas
print(f"Formato: {df.shape}")

# Verifica os tipos de dados
print(f"Tipos: {df.dtypes}")

# Verifica a quantidade de valores nulos
print(f"Nulos: {df.isnull().sum()}")