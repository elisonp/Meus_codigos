

# Pega o XPath do iframe e atribui a uma variável
iframe_1 = driver.find_element("xpath","/html/body/div[5]/div[2]/iframe")

# Muda o foco para o iframe
driver.switch_to.frame(iframe_1)

# Retorna para a janela principal (fora do iframe)
driver.switch_to.default_content()


#       ATENÇÃO
'''
    Caso encontre o cenário que tem mais de um iframe, você deverá
voltar a janela principal, com o comando da linha 10 e então criar
uma outra variável como o da linha 4 e então mover o foco para o novo
iframe criado, e alterando para ele como na linha 7.
'''