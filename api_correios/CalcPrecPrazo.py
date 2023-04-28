# import requests
# import json
# import os
# from dotenv import load_dotenv

# # Carrega as variáveis de ambiente do arquivo .env
# load_dotenv()

# # Obtém a chave de acesso à API dos Correios a partir da variável de ambiente
# chave = os.getenv('CHAVE_DE_ACESSO')

# # Define a URL da API dos Correios
# url_api = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente'

# # Define os parâmetros para o cálculo do preço e prazo de entrega
# cep_origem = '59076410' # CEP de origem da encomenda
# cep_destino = '89683000' # CEP de destino da encomenda
# peso = '1' # Peso da encomenda em quilogramas
# comprimento = '20' # Comprimento da encomenda em centímetros
# largura = '20' # Largura da encomenda em centímetros
# altura = '20' # Altura da encomenda em centímetros
# servico = '40010' # Código do serviço de encomenda a ser consultado

# # Define os parâmetros da requisição para a API dos Correios
# parametros = {'nCdEmpresa': '', 'sDsSenha': '', 'nCdServico': servico, 'sCepOrigem': cep_origem, 'sCepDestino': cep_destino, 'nVlPeso': peso, 'nCdFormato': 1, 'nVlComprimento': comprimento, 'nVlAltura': altura, 'nVlLargura': largura}

# # Define o cabeçalho da requisição para a API dos Correios
# cabecalho = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + chave}

# # Realiza uma requisição POST para a API dos Correios
# response = requests.post(url_api, data=json.dumps(parametros), headers=cabecalho)

# # Verifica se a requisição foi bem sucedida
# if response.status_code == 200:
#     # Exibe o preço e prazo de entrega retornado pela API dos Correios
#     resultado = response.json()['Servicos'][0]
#     preco = resultado['Valor']
#     prazo = resultado['PrazoEntrega']
#     print('Preço: R$', preco)
#     print('Prazo de entrega:', prazo, 'dias úteis')
# else:
#     print('Erro ao consultar a API dos Correios:', response.status_code)

import requests
import json

# Define a URL da API dos Correios
url_api = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente'

# Define os parâmetros para o cálculo do preço e prazo de entrega
cep_origem = '59076410' # CEP de origem da encomenda
cep_destino = '89683000' # CEP de destino da encomenda
peso = '1' # Peso da encomenda em quilogramas
comprimento = '20' # Comprimento da encomenda em centímetros
largura = '20' # Largura da encomenda em centímetros
altura = '20' # Altura da encomenda em centímetros
servico = '40010' # Código do serviço de encomenda a ser consultado

# Define os parâmetros da requisição para a API dos Correios
parametros = {'nCdEmpresa': '', 'sDsSenha': '', 'nCdServico': servico, 'sCepOrigem': cep_origem, 'sCepDestino': cep_destino, 'nVlPeso': peso, 'nCdFormato': 1, 'nVlComprimento': comprimento, 'nVlAltura': altura, 'nVlLargura': largura}

# Define o cabeçalho da requisição para a API dos Correios
cabecalho = {'Content-type': 'application/json', 'Accept': 'application/json'}

# Realiza uma requisição POST para a API dos Correios
response = requests.post(url_api, data=json.dumps(parametros), headers=cabecalho)



# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    # Exibe o preço e prazo de entrega retornado pela API dos Correios
    resultado = response.json()['Servicos'][0]
    preco = resultado['Valor']
    prazo = resultado['PrazoEntrega']
    print('Preço: R$', preco)
    print('Prazo de entrega:', prazo, 'dias úteis')
else:
    print('Erro ao consultar a API dos Correios:', response.status_code)
