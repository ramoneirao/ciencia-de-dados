import pandas as pd

df = pd.read_csv('Base de Dados/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verficação inicial: ')
print(df.info())

print(f'Análise de nulos: \n{df.isnull().sum()}\n')
print(f"Porcentagem de nulos: \n{df.isnull().mean() * 100}\n")
df.dropna(inplace=True)
print(f'Confirmando a remoção de nulos: \n{df.isnull().sum().sum()}\n')

print(f'Análise de duplicados: \n{df.duplicated().sum()}\n')

print(f"Anlise de dados unicos: \n{df.nunique()}\n")

print(f'Estatistica dos dados: \n{df.describe()}\n')

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('Base de Dados/clientes-v2-tratados.csv', index=False)