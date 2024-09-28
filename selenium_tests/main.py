from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
usuario = ""
senha = ""
slideDescription = input("Digite o tema do slide: ")

# Configurar o Chrome para rodar em segundo plano (headless mode)
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")

driver_path = "./chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.magicslides.app/pt/signin?source=%2F')

def login(driver, usuario, senha):
    try:
        wait = WebDriverWait(driver, 20)

        # Localizar e preencher o email
        signin_email = wait.until(EC.presence_of_element_located((By.ID, "email")))
        signin_email.click()
        signin_email.send_keys(usuario)

        # Localizar e preencher a senha
        signin_password = driver.find_element(By.ID, 'password')
        signin_password.click()
        signin_password.send_keys(senha)

        time.sleep(2)

        # Clicar no botão "Sign In"
        driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
        time.sleep(3)

        # Inserir descrição do slide
        descricao = wait.until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
        descricao.click()
        descricao.send_keys(slideDescription)

        # Tentar encontrar o botão correto e clicar
        #botao_gerar = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate Instant PPT')]")  # Ajuste o localizador conforme necessário
        #time.sleep(1)
        #botao_gerar.click()


        wait = WebDriverWait(driver, 20)

        # Localizando o botão pelo 'data-testid'
        botao_gerar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='send-button']")))

        # Clicando no botão
        botao_gerar.click()


        botao_next = wait.until(EC.element_to_be_clickable((By. ID, "generate-presentation-confirm")))
        botao_next.click()


        wait = WebDriverWait(driver, 20)
        div_elemento = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flex.gap-2.rounded-lg.border.p-3.bg-gray-50.border-gray-300")))

        div_elemento.click()

        botao_final = wait.until(EC.element_to_be_clickable((By. XPATH, "//button[contains(text(), 'Generate Presentation')]")))
        botao_final.click()
        wait = WebDriverWait(driver, 60)
        # Esperar até que o botão esteja clicável pelo ID
        download_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#headlessui-menu-button-\\:r6\\:')))
        # Clicar no botão
        download_button.click()

        ppt_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#headlessui-menu-item-\\:rb\\:')))
        ppt_button.click()  # Clicar no botão "PPT"

        #ppt_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate Presentation')]")))
        #ppt_button.click()  # Clicar no item PPT


        #button_finalle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "text-gray-700 block px-4 py-2 text-sm w-full text-left")))
        #button_finalle.click()







    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chamar a função de login
login(driver, usuario, senha)


