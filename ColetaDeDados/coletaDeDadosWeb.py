import requests
from bs4 import BeautifulSoup

url = "https://wiki.python.org.br/AprendaMais"
response = requests.get(url)
extracao = BeautifulSoup(response.text, 'html.parser')  

#Exibindo o texto
# print(extracao.text.strip())

# Filtrando as tags
con1 = 0
for linhas in extracao.find_all('h2'):
    titulo = linhas.text.strip()
    #print(f"Título: {titulo}")
    con1 += 1
print(f"Total de títulos: {con1}")  

con2 = 0
for linhas in extracao.find_all('p'):
    paragrafo = linhas.text
    #print(f"Parágrafo: {paragrafo}")
    con2 += 1
print(f"Total de parágrafos: {con2}")