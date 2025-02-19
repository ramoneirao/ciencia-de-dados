import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('Base de Dados/clientes-v2-tratados.csv')
print(df.head())

# Transformação Logarítmica
df['salario_log'] = np.log1p(df['salario'])  # log1p é usado para evitar problemas com valores 0
print(f'\nDataFrame após transformção logarítimica no salário:\n {df.head()}')

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)
print(f'\nDataFrame após transformção Box-Cox no salário: \n{df.head()}')

# Codificação de Frequência para 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)
print(f'\nDataFrame após codificação de frequência para o estado: \n{df.head()}')

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print(f'\nDataFrame após adição da interação entre idade e quantidade de filhos: \n{df.head()}')
