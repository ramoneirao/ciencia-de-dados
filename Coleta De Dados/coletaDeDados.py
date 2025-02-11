import requests 
from bs4 import BeautifulSoup 
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "https://finance.yahoo.com/quote/%5EBVSP/history/"
response = requests.get(url, headers=headers)
#print(response.text[:600])

soup = BeautifulSoup(response.text, 'html.parser')  
#print(soup.prettify()[:1000])
tables = soup.find_all("table")

if tables:
    df = pd.read_html(str(tables[0]))[0]  # Convertendo a primeira tabela para DataFrame
    print(df.head(10))
else:
    print("Nenhuma tabela encontrada.")

print(df.shape)
