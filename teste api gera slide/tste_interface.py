import customtkinter as ctk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# Função principal para o processo de login e geração de slides
def gerar_slides():
    
    #gerarslides@gmail.com   --  profile 3
    #gerarslides2@gmail.com  --  profile 2
    #gerarslides4@gmail.com  --  profile 4 -- senha Ger4@rslides12#
    #gerarslides5@gmail.com  --  profile 5
    usuario = "gerarslides@gmail.com"
    senha = "Ger4@slides12"
    slideDescription = tema_var.get()

    if not slideDescription:
        messagebox.showerror("Erro", "Por favor, insira um tema para os slides.")
        return

    # Configurar o Chrome para rodar em segundo plano (headless mode)
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    profile_path = r'C:\Users\Victor\AppData\Local\Google\Chrome\User Data\Profile 3'
    chrome_options.add_argument(f"user-data-dir={profile_path}")

    driver_path = "./chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://gamma.app/create/generate')

    try:
        wait = WebDriverWait(driver, 20)

        # Interação com os campos do site
        time.sleep(5)
        textarea = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@class, 'chakra-textarea')]")))
        textarea.send_keys(slideDescription)

        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-y0msvc")))
        button.click()

        continuar = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continuar')]")))
        continuar.click()

        gerar_final = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Gerar')]")))
        gerar_final.click()
        time.sleep(40)

        button_menu = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='doc-toolbar-menu-button']")))
        button_menu.click()

        botao_export = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[span[contains(text(), 'Exportar...')]]")))
        botao_export.click()



        wait = WebDriverWait(driver, 40)

        div_exportar = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class, 'css-1qrkfiv')]//p[text()='Exportar para PowerPoint']")))
        div_exportar.click()

        time.sleep(40)
        messagebox.showinfo("Sucesso", "Slides gerados com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    finally:
        driver.quit()


# Função para sair do aplicativo
def sair():
    root.quit()


# Interface gráfica usando customtkinter
ctk.set_appearance_mode("dark")  # Define o tema como claro
ctk.set_default_color_theme("blue")  # Define um tema padrão

root = ctk.CTk()
root.title("Gerador de Slides Automático")

# Definir o tamanho da janela
root.geometry("500x250")

# Aplicar o tema roxo customizado


# Título da interface
titulo_label = ctk.CTkLabel(root, text="Gerador de Slides Hudson - Sanofi", font=("Arial", 20), text_color="white")
titulo_label.pack(pady=10)

# Campo para input do tema
tema_label = ctk.CTkLabel(root, text="Digite o tema do slide:", text_color="white")
tema_label.pack(pady=5)

tema_var = ctk.StringVar()
tema_entry = ctk.CTkEntry(root, textvariable=tema_var, width=300, height=40, corner_radius=10)
tema_entry.pack(pady=5)

# Botão para gerar slides
gerar_button = ctk.CTkButton(root, text="Gerar Slides", command=gerar_slides, width=150, height=40, corner_radius=10,
                             fg_color="#06420b")
gerar_button.pack(pady=10)

# Botão para sair
sair_button = ctk.CTkButton(root, text="Sair", command=sair, width=150, height=40, corner_radius=10, fg_color="#570707")
sair_button.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
