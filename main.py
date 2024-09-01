from AFD.afd import ler_arquivo
from APD.apd import ler_arquivo_apd

def menu():
    print("Selecione uma máquina de estados:")
    print("1 - AFD\n2 - APD\n3 - APN")
    maquina = int(input())

    if(maquina == 1):
        caminho = "AFD/maquina3.txt"
        print(caminho)
        afd = ler_arquivo(caminho)
        if afd.processar_input():
            print("Poção concluida com sucesso!")
        else:
            print("Erro na poção!")
    elif(maquina == 2):
        caminho = "APD/maquina_APD2.txt"
        print(caminho)
        apd = ler_arquivo_apd(caminho)

        # Testando o APD com uma cadeia
        if apd.processar_input_apd():
            print("Poção concluida com sucesso!")
        else:
            print("Erro na poção!")

        
menu()