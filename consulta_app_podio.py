import pandas as pd
#importando biblioteca podio.
from pypodio2 import api
from pypodio2.transport import TransportException
from tools_VTec.podio_tools import handlingPodioError

import os
#Importando bibioteca para conseguir ler arquivo env.
from dotenv import load_dotenv
#Importando um biblioteca local com funções de banco de dados.

import time

#Função recebe o json 'field' e extrai o valor do mesmo
def get_field_values(field):
	value = ""
	if field['type'] == "contact":
		# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
		# Podem haver aspas duplas inseridas no valor do campo. Substituir com aspas simples
		for elem in field['values']:
			value += elem['value']['name'].replace("\"", "'") + "|"
		value = value[:-1]
	elif field['type'] == "category":
		value += field['values'][0]['value']['text'].replace("\"", "'")
	elif field['type'] == "date" or (field['type'] == "calculation" and 'start' in \
		field['values'][0]):
		value += field['values'][0]['start']
	elif field['type'] == "money":
		value += field['values'][0]['currency'] + " " + field['values'][0]['value']
	elif field['type'] == "image":
		value += field['values'][0]['value']['link']
	elif field['type'] == "embed":
		value += field['values'][0]['embed']['url']
	elif field['type'] == "app":
		# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
		for val in field['values']:
			value += val['value']['title'].replace("\"", "'") + "|"
		value = value[:-1]
	elif field['type'] == "number":
		value += str(float(field['values'][0]['value']))
	else:
		value += str(field['values'][0]['value']).replace("\"", "'")
	
	return value
	
def consultar_dados():
	load_dotenv()
	#Credenciais de acesso ao podio
	client_id = os.getenv('PODIO_CLIENT_ID')
	client_secret = os.getenv('PODIO_CLIENT_SECRET')
	username = os.getenv('PODIO_USERNAME')
	password = os.getenv('PODIO_PASSWORD')

	#Conectando ao PODIO via API, com as credenciais de acesso acima.
	#def Autenticar_podio(self,client_id,client_secret, username, password):
	#	self.podio = api.OAuthClient(client_id,client_secret,username,password)
	podio = api.OAuthClient(client_id,client_secret,username,password)
	solicitar_dados_appid = 27731627	
	app_info = podio.Application.find(solicitar_dados_appid)


	#Constroi as colunas do dataframe a partir dos campos do aplicativo que vem em formato Json, mas já como dict
	column_labels = []
	for field in app_info.get('fields'):
		if field['status'] == "active":
			label = field['external_id']
			label = label[:30]#Quantidade de caracteres que pode ter em cada coluna
			column_labels.append(label)
	#Obtendo os itens 
	#offset = A partir de
	#limite, por padrão é 500
	#sorte_by ordernar por data de criação

	num_of_items = podio.Application.get_items(app_info.get('app_id'))['total']

	#Dados do dataframe
	datatable = []
	try:
		for step in range(0, num_of_items, 250):
			filtered_items = podio.Item.filter(app_info.get('app_id'), {"offset": step, "sort_by": "created_on", "sort_desc": False, "limit": 250})

			items = filtered_items.get('items')
			total = filtered_items.get('total')

			#for item in items:
			for item in items:
				row = []
				#adicionando os valores item_id 
				row.append(str(item['item_id']))
				row.append(str(item['created_on']))
				#row.append(str(item['file_id']))
				#Variavel utilizada para comparar
				fields = [x for x in item['fields'] if f"{x['external_id'][:40]}" in column_labels]
				# Fazendo a comparação entre os campos existentes e os preenchidos
				# Caso o campo esteja em branco no Podio, preencher com '?'
				item_iterador = 0
				for app_iterador in range(len(column_labels)):
					col_value = ""
					if item_iterador < len(fields) and str(fields[item_iterador]['external_id'][:40]) == column_labels[app_iterador]:
						col_value = get_field_values(fields[item_iterador])
						item_iterador += 1
					row.append(col_value)
				datatable.append(row)
		############# Valores Armazenados no APP ###############
		df_app = pd.DataFrame(datatable,columns=['item-id', 'created-on']+column_labels)

		for i in df_app.index:
							
			#print((df_app['item-id'][i]))
			print('Acessando o item: '+str(df_app['id'][i]))

			#Encontra os chaves e valores dos items
			item_id = podio.Item.find(int(df_app['item-id'][i]))
			
	except TransportException as err:
		handled = handlingPodioError(err)
		if handled == 'rate_limit':
			return 2
			print('limite de requisições, esperando uma hora para continuar...')
			time.sleep(3600)
