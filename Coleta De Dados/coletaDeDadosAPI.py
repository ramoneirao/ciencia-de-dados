import requests
import json

def enviar_arquivo():
    # Caminho do arquivo para upload 
    caminho = r"C:/Users/ramon/Downloads/produtos_informatica.xlsx"

    # Enviar arquivo
    requisicao = requests.post("https://file.io", files={"file": open(caminho, "rb")})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao["link"]
    print(f"Link para download: {url}")


enviar_arquivo()
