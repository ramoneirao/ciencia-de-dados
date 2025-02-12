import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Base de Dados\clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão Escolaridade 1')
plt.xlabel('Nível Educacional')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão Escolaridade 2')
plt.xlabel('Nível Educacional')
plt.ylabel('Quantidade')

# Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação')
plt.show()

# Gráfico de dispersão
# https://matplotlib.org/stable/users/explain/colors/colormaps.html
plt.hexbin(df['idade'], df['salario'], gridsize=20, cmap='Greens')
plt.colorbar(label='Contagem dentro do bin')
plt.title('Dispersão - Idade e Salário')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()  

