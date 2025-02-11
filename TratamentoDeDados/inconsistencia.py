import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('Base De Dados/clientes_sem_outliers.csv')
print(df.head())

# Mascarando dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda x: x[:3] + '***.***.***-' + x[-2:])

# Corrigir Datas
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, df['data'] - pd.to_datetime('1900-01-01'))
df['idade_ajustada']  = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

# Corrigindo campos com multiplas informações
df['endereco_curto'] = df['endereco'].apply(lambda x : x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x : x.split('\n')[1].strip() if len(x.split('\n')) > 1 else "Desconhecido")
df['estadoSigla'] = df['endereco'].apply(lambda x : x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else "Desconhecido")

# Verificando a formatação de endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x : "Endereço inválido" if len(x) > 50 or len(x) < 5 else x)

# Corrigir dados erroneos 
df['cpf'] = df['cpf'].apply(lambda x :x if len(x) == 14 else "CPF inválido")

estadosBR = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estadoSigla'] = df['estadoSigla'].str.upper().apply(lambda x : x if x in estadosBR else "Estado inválido")

print("Dados Tratados: \n")
df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['data'] = df['data_atualizada']
df['estado'] = df['estadoSigla']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'bairro', 'estado']]
print(df.shape)

df_salvar.to_csv('Base De Dados/clientes_tratados.csv', index=False)