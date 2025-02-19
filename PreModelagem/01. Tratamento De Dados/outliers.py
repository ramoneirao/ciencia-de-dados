import pandas as pd
from scipy import stats

pd.set_option('display.width', None)
df = pd.read_csv('Base de Dados/clientes_limpos.csv')

df_filtro_basico = df[df['idade'] > 100]

print(f'Filtro básico \n {df_filtro_basico[['nome', 'idade']]}')

# Identificar outliers com Z-Score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[(z_scores >= 3)]
print(f'Outliers pelo Z-Score:\n{outliers_z}')

# Filtrando com Z-Score
df_ZScore = df[(stats.zscore(df['idade']) < 3)]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print(f'Limite baixo: {limite_baixo} \nLimite alto: {limite_alto}')

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print(f'Outliers pelo IQR:\n{outliers_iqr}')

# Filtrando com IQR
df_IQR = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

limite_alto = 100
limite_baixo = 0

df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtrnado inválidos 
df['endereco'] = df['endereco'].apply(lambda x: "Endereço inválido" if len(x.split('\n')) < 3 else x)
print(f"Quantidade de endereços inválidos: {(df['endereco'] == 'Endereço inválido').sum()}")

# Tratar campos de Texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print(f"Quantidade de nomes inválidos: {(df['nome'] == 'Nome inválido').sum()}")

print(f"Dados com os Outliers removidos: \n{df}")

# Salvando os dados
df.to_csv('Base de Dados/clientes_sem_outliers.csv', index=False)