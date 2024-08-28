from AFD.afd import ler_arquivo

def menu():
    print("Selecione uma máquina de estados:")
    print("1 - AFD")
    maquina = int(input())
    caminho = "AFD/afd.txt"
    
    if(maquina == 1):
        print(caminho)
        afd = ler_arquivo(caminho)
        afd.processar_input()

menu()