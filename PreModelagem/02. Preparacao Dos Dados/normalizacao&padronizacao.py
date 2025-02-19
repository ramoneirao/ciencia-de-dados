import pandas as pd
from sklearn.preprocessing import RobustScaler, StandardScaler, MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('Base de Dados/clientes-v2-tratados.csv')

print(df.head())

df = df.drop(['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis = 1)

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler-mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler-mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Normalização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print("MinMaxScaler (De 0 a1):")
print(f"Idade - Min {df['idadeMinMaxScaler'].min():.4f} Max {df['idadeMinMaxScaler'].max():.4f} Média: {df['idadeMinMaxScaler'].mean():.4f} Std: {df['idadeMinMaxScaler'].std():.4f}")
print(f"Salário - Min {df['salarioMinMaxScaler'].min():.4f} Max {df['salarioMinMaxScaler'].max():.4f} Média: {df['salarioMinMaxScaler'].mean():.4f} Std: {df['salarioMinMaxScaler'].std():.4f}")

print("\nMinMaxScaler (-1 a 1):")
print(f"Idade - Min {df['idadeMinMaxScaler-mm'].min():.4f} Max {df['idadeMinMaxScaler-mm'].max():.4f} Média: {df['idadeMinMaxScaler-mm'].mean():.4f} Std: {df['idadeMinMaxScaler-mm'].std():.4f}")
print(f"Salário - Min {df['salarioMinMaxScaler-mm'].min():.4f} Max {df['salarioMinMaxScaler-mm'].max():.4f} Média: {df['salarioMinMaxScaler-mm'].mean():.4f} Std: {df['salarioMinMaxScaler-mm'].std():.4f}")

print("\nStandardScaler (Ajuste a média a 0 e desvio padrão a 1):")
print(f"Idade - Min {df['idadeStandardScaler'].min():.4f} Max {df['idadeStandardScaler'].max():.4f} Média: {df['idadeStandardScaler'].mean():.4f} Std: {df['idadeStandardScaler'].std():.4f}")
print(f"Salário - Min {df['salarioStandardScaler'].min():.4f} Max {df['salarioStandardScaler'].max():.4f} Média: {df['salarioStandardScaler'].mean():.4f} Std: {df['salarioStandardScaler'].std():.4f}")

print("\nRobustScaler (Ajuste a mediana e IQR):")
print(f"Idade - Min {df['idadeRobustScaler'].min():.4f} Max {df['idadeRobustScaler'].max():.4f} Média: {df['idadeRobustScaler'].mean():.4f} Std: {df['idadeRobustScaler'].std():.4f}")
print(f"Salário - Min {df['salarioRobustScaler'].min():.4f} Max {df['salarioRobustScaler'].max():.4f} Média: {df['salarioRobustScaler'].mean():.4f} Std: {df['salarioRobustScaler'].std():.4f}")
