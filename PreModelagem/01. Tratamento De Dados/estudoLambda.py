import pandas as pd

#Função para calcular o cubo de um número 
def cubo(x):
    return x**3


# Expressão lambda para calcular o cubo de um número
cuboLambda = lambda x: x**3

print(cubo(2))
print(cuboLambda(2))

# Criando um DataFrame
df = pd.DataFrame({'Números': [1, 2, 3, 4, 5, 10]})

df['Cubo'] = df['Números'].apply(cubo)
df['CuboLambda'] = df['Números'].apply(lambda x: x**3)  # ou .apply(cuboLambda)

print(df.head(6))