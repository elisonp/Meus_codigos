# Pega o XPath do iframe e atribui a uma variável
iframe = driver.find_element_by_xpath("//*[@id="editor"]/div[3]/div[3]/iframe")

# Muda o foco para o iframe
driver.switch_to.frame(iframe)

# Retorna para a janela principal (fora do iframe)
driver.switch_to.default_content()