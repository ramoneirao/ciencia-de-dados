import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')
dados_pessoas = []

# Gerando dados fictícios
for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y')
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data_nascimento': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)

df = pd.DataFrame(dados_pessoas)
print(df)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print(df.to_string())

df.to_csv('clientes.csv',)