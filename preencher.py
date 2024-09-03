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
driver.get('https://adm.donphellipe.com.br/sourceCode/pages/Adm/login/index.html')  # Substitua com a URL real

# Preenche o primeiro campo
campo1 = driver.find_element(By.ID, 'inputEmail')  # Substitua com o ID real
campo1.send_keys('dono@gmail.com')

# Preenche o segundo campo
campo2 = driver.find_element(By.ID, 'inputSenha')  # Substitua com o ID real
campo2.send_keys('adm12345')

input("Por favor, resolva o CAPTCHA e pressione Enter para continuar...")

# Envia o formulário
campo2.send_keys(Keys.RETURN)  # Envia o formulário ao pressionar Enter no segundo campo

# Aguarda a mudança de página
time.sleep(10)  # Espera 5 segundos, ajuste conforme necessário

# Fecha o navegador
driver.quit()
