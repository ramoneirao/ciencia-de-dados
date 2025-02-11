import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# Removendo dados
df.drop('pais', axis=1, inplace=True)  # Coluna
df.drop(2, axis=0, inplace=True)  # Linha

# Normalizar os campos de texto 
df['nome']      = df['nome'].str.title()
df['endereco']  = df['endereco'].str.lower()
df['estado']    = df['estado'].str.strip().str.upper()

# Converter os tipos de dados
df['idade'] = df['idade'].astype(int)

# Tratando os valores nulos 
df_fillna = df.fillna(0) # Preenche com 0
df_dropna = df.dropna()  # Remove os valores nulos
df_dropna4 = df.dropna(thresh=4)  # Remove as linhas que possuem 4 ou mais valores nulos
df = df.dropna(subset=['cpf'])  # Remove as linhas com o CPF nulo

print(f"Valores Nulos: {df.isnull().sum()}")
print(f"Quantidade de valores nulos com fillna: {df_fillna.isnull().sum()}")
print(f"Quantidade de valores nulos com dropna: {df_dropna.isnull().sum()}")
print(f"Quantidade de valores nulos com dropna4: {df_dropna4.isnull().sum()}")
print(f"Quantidade de valores nulos com drop: {df.isnull().sum()}")

df.fillna({'estado' : 'Desconhecido'}, inplace=True)  # Preenche os valores nulos do estado com 'Desconhecido'
df['endereco'] = df['endereco'].fillna('Endereço não informado!')  # Preenche os valores nulos do endereço com 'Endereço não informado!'
df['idadeCorrigida'] = df['idade'].fillna(df['idade'].mean())  # Preenche os valores nulos da idade com a média das idades

#Tratar formatos de dados
df['dataCorrgida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Tratando dados duplicados
print(f"Qunatidade de registros atuais: {df.shape[0]}")
df.drop_duplicates(subset='cpf', inplace=True)
print(f"Qunatidade de registros após a remoção: {len(df)}")

print(f"Dados limpos: {df.head()}")

# Salvando os dados
df['data'] = df['dataCorrgida']
df['idade'] = df['idadeCorrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpos.csv', index=False)


print(f"Arquivo salvo com sucesso!\n",
      f"Novo DataFrame:\n {pd.read_csv('clientes_limpos.csv')}")
