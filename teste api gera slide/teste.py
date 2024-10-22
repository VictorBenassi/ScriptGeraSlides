from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from spyder.plugins.help.utils.sphinxify import CSS_PATH
from webdriver_manager.drivers.edge import EdgeChromiumDriver

# "gerarslides@gmail.com"  - senha: Ger4@slides12
#gerarslides@outlook.pt#
#Gera@slides1#
usuario = "gerarslides@gmail.com"
senha = "Ger4@slides12"
slideDescription = input("Digite o tema do slide: ")

# Configurar o Chrome para rodar em segundo plano (headless mode)
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Modo headless
#chrome_options.add_argument("--disable-gpu")  # Acelera o headless em alguns casos
#chrome_options.add_argument("--no-sandbox")  # Necessário para Linux em algumas situações
chrome_options.add_argument("--window-size=1920x1080")  # Define o tamanho da janela no modo headless
#./chromedriver.exe#
#./msedgedriver.exe#
profile_path = r'C:\Users\Victor\AppData\Local\Google\Chrome\User Data\Profile 1'
chrome_options.add_argument(f"user-data-dir={profile_path}")

driver_path = "./chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://gamma.app/create/generate')

def login(driver, usuario, senha):
    try:
        wait = WebDriverWait(driver, 20)
        # Esperar a página carregar antes de interagir (ajustar conforme necessário)

        # Encontrar o campo de email e preencher
       # email_field = wait.until(EC.presence_of_element_located((By.ID, 'email')))
       # email_field.send_keys(usuario)

        # Encontrar o campo de senha e preencher
        #password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        #password_field.send_keys(senha + Keys.ENTER)
        # Clicar no botão de login
        #login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Entrar')]")))
        #login_button.click()
        # Esperar até a página carregar após o login


        #password_field.send_keys(Keys.TAB)  # Primeiro TAB
        #time.sleep(1)
        #password_field.send_keys(Keys.TAB)  # Segundo TAB
        #time.sleep(1)
        #password_field.send_keys(Keys.ENTER)  # ENTER

        #apresentacao = driver.find_element(By.CLASS_NAME, "chakra-button chakra-stack css-1iu9wmc")
        #apresentacao.click()
        #driver.send_keys(Keys.TAB *5)
        time.sleep(5)
        #texto = driver.find_element(By.XPATH, "//textarea[@placeholder='Descreva o que gostaria de fazer']")
        #texto.click()
        #driver.send_keys(slideDescription)

        wait = WebDriverWait(driver, 20)
        textarea = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@class, 'chakra-textarea')]")))
        textarea.send_keys(slideDescription)

        wait = WebDriverWait(driver, 20)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-y0msvc")))
        button.click()

        continuar = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continuar')]")))
        continuar.click()

        gerar_final = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Gerar')]")))
        gerar_final.click()
        time.sleep(40)

        wait = WebDriverWait(driver, 20)
        button_menu = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='doc-toolbar-menu-button']")))
        button_menu.click()



        wait = WebDriverWait(driver, 20)
        botao_export =wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[contains(text(), 'Exportar...')]]")))
        botao_export.click()



        #wait = WebDriverWait(driver, 20)
        #div_formato = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1qrkfiv")))
        #div_formato.click()

        wait = WebDriverWait(driver, 15)
        div_exportar = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'css-1qrkfiv')]//p[text()='Exportar para PowerPoint']")))
        div_exportar.click()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")








# Chamar a função de login
login(driver, usuario, senha)

time.sleep(240)




# Fechar o navegador
#driver.quit()
