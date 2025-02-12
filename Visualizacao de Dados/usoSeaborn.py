import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Base de Dados/clientes-v3-preparado.csv')
print(df.head())

# Gráfico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') # ['scatter', 'reg', 'resid', 'kde', 'hex', 'hist']
plt.show()

# Grafico de Densidade 
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])  # https://seaborn.pydata.org/tutorial/color_palettes.html
plt.show()

# Gráfico de Regressão
sns.regplot(x='idade', y='salario', data=df, color='#287f65')
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico com Countplot
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nível de Educação')
plt.show()
