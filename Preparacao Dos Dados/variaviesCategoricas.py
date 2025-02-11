import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('Base de Dados/clientes-v2-tratados.csv')

# Codificação one-hot para 'estado_civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print(f"\nDataFrame após codificação one-hot para estado_civil:\n{df.head()}")  

# Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-Graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print(f"\nDataFrame após codificação ordinal para nivel_educacao:\n{df.head()}")

# Trnsformar 'area_atuacao' em categorias codificadas usando o método .cat.codes    
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print(f"\nDataFrame após codificação para area_atuacao:\n{df.head()}")

# LabelEncoder para 'estado'
# LabelEncoder convert cada valor único em números de 0 a n_classes-1
labelencoder = LabelEncoder()
df['estado_cod'] = labelencoder.fit_transform(df['estado'])

print(f"\nDataFrame após codificação para estado:\n{df.head()}")
