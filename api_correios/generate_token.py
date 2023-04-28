import requests
from requests.auth import HTTPBasicAuth
import json, os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def new_token():
    
    # Obtém a chave de acesso à API dos Correios a partir da variável de ambiente
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')

    # URL para a obtenção do token de acesso
    url = "https://api.correios.com.br/token/v1/autentica"

    headers = {
    'Content-Type': 'application/json'
    }

    # response = json.loads(requests.request("POST", url, headers=headers, data=payload).text)
    response = requests.request("POST", url = url, headers=headers, auth=HTTPBasicAuth(user, password))
    
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 201:
        # Exibe o token de acesso retornado pela API dos Correios
        token_acesso = response.json()['token']
        print('Token de acesso:', token_acesso)
        
    else:
        print('Erro ao obter o token de acesso:', response.status_code)

new_token()
