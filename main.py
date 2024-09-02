from AFD.afd import ler_arquivo
from APD.apd import ler_arquivo_apd
from MOORE.moore import ler_arquivo_moore
from MEALY.mealy import ler_arquivo_mealy

def menu():
    print("Selecione uma máquina de estados:")
    print("1 - AFD\n2 - APD\n3 - Moore")
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

        if apd.processar_input_apd():
            print("Poção concluida com sucesso!")
        else:
            print("Erro na poção!")
    elif(maquina == 3):
        caminho = "MOORE/moore.txt"
        print(caminho)
        moore = ler_arquivo_moore(caminho)

        moore.processar_input_moore()
    elif(maquina == 4):
        caminho = "MEALY/mealy.txt"
        print(caminho)
        mealy = ler_arquivo_mealy(caminho)

        mealy.processar_input_mealy()
        
menu()