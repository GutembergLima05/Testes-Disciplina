from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o serviço do ChromeDriver
service = Service(ChromeDriverManager().install())

# Cria uma instância do navegador
driver = webdriver.Chrome(service=service)

# Navega para o site
driver.get('http://127.0.0.1:5500/1000/index.html')

# Lista de dados para preencher o formulário
dados = [
    {'name': 'Monkey Last', 'username': 'monkey.last', 'password': 'adm12345', 'confirm_password': 'adm12345'},
    {'name': 'Lion Good', 'username': 'lion.good', 'password': 'adm12345', 'confirm_password': 'adm12345'},
    {'name': 'Pig Zumbi', 'username': 'pig.zumbi', 'password': 'adm12345', 'confirm_password': 'adm12345'}
]

# Itera sobre os dados e preenche o formulário
for dado in dados:
    # Preenche o primeiro campo
    campo1 = driver.find_element(By.ID, 'name')
    campo1.clear()  # Limpa o campo antes de preencher
    campo1.send_keys(dado['name'])
    time.sleep(1)

    # Preenche o segundo campo
    campo2 = driver.find_element(By.ID, 'username')
    campo2.clear()  # Limpa o campo antes de preencher
    campo2.send_keys(dado['username'])
    time.sleep(1)

    # Preenche o terceiro campo
    campo3 = driver.find_element(By.ID, 'password')
    campo3.clear()  # Limpa o campo antes de preencher
    campo3.send_keys(dado['password'])
    time.sleep(1)

    # Preenche o quarto campo
    campo4 = driver.find_element(By.ID, 'confirm_password')
    campo4.clear()  # Limpa o campo antes de preencher
    campo4.send_keys(dado['confirm_password'])
    time.sleep(1)

    # Envia o formulário
    campo4.send_keys(Keys.RETURN)
    time.sleep(5)  # Aguarda a mudança de página ou qualquer outro processo

    # Volta para a página de formulário para a próxima iteração
    driver.get('http://127.0.0.1:5500/1000/index.html')

# Fecha o navegador
driver.quit()
