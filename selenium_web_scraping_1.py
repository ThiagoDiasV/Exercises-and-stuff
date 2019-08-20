from selenium import webdriver
from time import sleep

# Definição de variáveis
url = 'https://www2.cjf.jus.br/jurisprudencia/unificada/'
search_bar = 'formulario:textoLivre'  # id

search_button = 'formulario:actPesquisar'  # id button
simple_information_button = 'formulario:lista_resumida'  # id
all_options = 'formulario:checkTodos'  # id
all_tru_button = 'formulario:todasTRUs'  # id
all_tr_button = 'formulario:todasTRs'  # id

lista_botoes = [simple_information_button, 
                all_options, 
                all_tru_button, 
                all_tr_button,
                search_button]

# Abrir o firefox
ff = webdriver.Firefox()

# Abrir a url
ff.get(url)

# Definindo o que vai ser pesquisado
ff.find_element_by_id(search_bar).send_keys('Assalto mão armada')

# Clicando em todos os botões
for botao in lista_botoes:
    ff.find_element_by_id(botao).click()
    sleep(3)

sleep(15)
ff.quit()
