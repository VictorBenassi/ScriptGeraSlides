import time
import sys
import threading


# Função de carregamento em paralelo
def carregando(flag):
    while flag.is_set():
        for i in range(4):
            if not flag.is_set():
                break
            sys.stdout.write("\rCarregando" + "." * i)
            sys.stdout.flush()
            time.sleep(0.5)


# Função login simulada (você pode substituir com a implementação real)
def login(driver, usuario, senha):
    # Simulação do processo de login (substitua pelo código real)
    time.sleep(5)  # Simula tempo de login
    return True


# Função principal
def main():
    flag = threading.Event()
    flag.set()

    # Inicia o carregamento em uma thread separada
    thread = threading.Thread(target=carregando, args=(flag,))
    thread.start()

    # Substitua esses parâmetros pelo seu código real de login
    driver = None  # Simulação de driver
    usuario = "usuario_exemplo"
    senha = "senha_exemplo"

    # Chama a função login
    login(driver, usuario, senha)

    # Quando o login finalizar, interrompe o carregamento
    flag.clear()

    # Aguarda a thread do carregamento finalizar
    thread.join()

    print("\nConcluído")


if __name__ == "__main__":
    main()

