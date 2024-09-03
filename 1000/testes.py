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
driver.get('http://127.0.0.1:5500/1000/index.html')  # Substitua com a URL real

# Preenche o primeiro campo
campo1 = driver.find_element(By.ID, 'name')  # Substitua com o ID real
campo1.send_keys('Gutemberg')

# Preenche o segundo campo
campo2 = driver.find_element(By.ID, 'username')  # Substitua com o ID real
campo2.send_keys('gutemberg.junior')

campo3 = driver.find_element(By.ID, 'password')  # Substitua com o ID real
campo3.send_keys('adm12345')

campo4 = driver.find_element(By.ID, 'confirm_password')
campo4.send_keys('adm12345')

# Envia o formulário
campo4.send_keys(Keys.RETURN)  # Envia o formulário ao pressionar Enter no segundo campo

# Aguarda a mudança de página
time.sleep(10)  # Espera 5 segundos, ajuste conforme necessário

# Fecha o navegador
driver.quit()
