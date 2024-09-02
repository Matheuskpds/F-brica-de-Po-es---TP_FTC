import os

tabela_maquina1 = """
╔══════════════════════════╦═════════╗
║       Ingrediente        ║ Símbolo ║
╠══════════════════════════╬═════════╣
║ água                     ║ a       ║
║ lagrimas de unicornio    ║ l       ║
║ folhas da arvore da vida ║ f       ║
║ escamas de dragao        ║ d       ║
╚══════════════════════════╩═════════╝
"""
pocao_maquina1 = {
    "Pocao": "Pocao da Luz",
    "Ingredientes": "a l f d",
    "descricao": "Cria um líquido viscoso com um brilho que dura até dias.",
    "modo_preparo": [
        "Comece adicionando a quantidade de água que desejar, porém apenas inicialmente.",
        "Em sequência adicione uma dose de lágrimas de unicórnio.",
        "Por fim, adicione uma folha da árvore da vida.",
        "Escamas de dragão causarão com que a poção falhe."
    ]
}

tabela_maquina2 = """
╔═══════════════════╦═════════╗
║    Ingrediente    ║ Símbolo ║
╠═══════════════════╬═════════╣
║ moedas de ouro    ║ m       ║
║ elixir            ║ e       ║
║ escamas de dragao ║ d       ║
╚═══════════════════╩═════════╝
"""
pocao_maquina2 = {
    "Pocao": "Pocao da resistencia ao fogo",
    "Ingredientes": "m e d",
    "descricao": "Cria uma poção que deixa uma pessoa ou objeto resistente a fogo, duração da resistência depende da quantidade de escamas de dragão utilizadas.",
    "modo_preparo": [
        "Comece adicionando uma porção de elixir.",
        "Em sequência adicione quantas vezes preferir, no mínimo uma escama de dragão e no máximo duas, sempre seguidas de moedas de ouro (três escamas de dragão seguidas, causará uma explosão)."
    ]
}

tabela_maquina3 = """
╔══════════════════════════╦═════════╗
║       Ingrediente        ║ Símbolo ║
╠══════════════════════════╬═════════╣
║ petalas de rosa          ║ p       ║
║ elixir                   ║ e       ║
║ lagrimas de unicornio    ║ l       ║
║ folhas da arvore da vida ║ f       ║
╚══════════════════════════╩═════════╝
"""
pocao_maquina3 = {
    "Pocao": "Pocao do amor",
    "Ingredientes": "p e l f",
    "descricao": "Cria uma poção do amor, que deixa o bebedor apaixonado por quem lhe deu a bebida.",
    "modo_preparo": [
        "Comece adicionando elixir.",
        "Em sequência adicione duas pétalas de rosa.",
        "A adição de mais elixir ou pétalas de rosa e outros ingredientes como lágrimas de unicórnio e folhas da árvore da vida pode ser feita sem restrições ao final da mistura para variação no gosto da bebida"
    ]
}

class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    
    def transicao(self, estado, simbolo):
        print("Transicao de ", estado, " com ", simbolo)
        return self.transicoes.get((estado, simbolo), None)
    
    def processar_input(self, caminho_do_arquivo):
        estado = self.estado_inicial # Estado atual, começa como o inicial


        resposta = 's' # Variavel para a resposta de inserir mais um ingrediente ou nao
        while True:
            if resposta == 's':
                os.system('cls')
                if(caminho_do_arquivo == "AFD/maquina1.txt"):
                    print(tabela_maquina1)
                    print("Pocao: ", pocao_maquina1["Pocao"])
                    print("Ingredientes(simbolos): ", pocao_maquina1["Ingredientes"])
                    print("Descrição da poção: ", pocao_maquina1["descricao"])
                    print("\nModo de preparo:")
                    for i in range(len(pocao_maquina1["modo_preparo"])):
                        print(i+1, "- ", pocao_maquina1["modo_preparo"][i])
                elif(caminho_do_arquivo == "AFD/maquina2.txt"):
                    print(tabela_maquina2)
                    print("Pocao: ", pocao_maquina1["Pocao"])
                    print("Ingredientes(simbolos): ", pocao_maquina2["Ingredientes"])
                    print("Descrição da poção: ", pocao_maquina2["descricao"])
                    print("\nModo de preparo:")
                    for i in range(len(pocao_maquina2["modo_preparo"])):
                        print(i+1, "- ", pocao_maquina2["modo_preparo"][i])
                elif(caminho_do_arquivo == "AFD/maquina3.txt"):
                    print(tabela_maquina3)
                    print("Pocao: ", pocao_maquina1["Pocao"])
                    print("Ingredientes(simbolos): ", pocao_maquina3["Ingredientes"])
                    print("Descrição da poção: ", pocao_maquina3["descricao"])
                    print("\nModo de preparo:")
                    for i in range(len(pocao_maquina3["modo_preparo"])):
                        print(i+1, "- ", pocao_maquina3["modo_preparo"][i])
                        
                simbolo = input("\nQual ingrediente será inserido:\n")
                
                print("\nEstado atual: ", estado)
                print("Simbolo atual: ", simbolo)
                estado = self.transicao(estado, simbolo) # Realiza a transicao dos estados
                if estado is None: # Caso nao exista a transicao, retorna falso
                    return False
            elif resposta == 'n':
                break
            else:
                print("Resposta inválida!")
            resposta = input("\nDeseja inserir mais um ingrediente(s/n)?\n")
            resposta = resposta.strip()
       
        print("\nEstado final: ", estado)
        return estado in self.estados_aceitacao # Procura se o estado que parou, é um estado final

def ler_arquivo(caminho_do_arquivo):
    print("Lendo arquivo ", caminho_do_arquivo) #Le o arquivo txt da maquina
    with open(caminho_do_arquivo, 'r') as arq:
        linhas = arq.readlines()
    
    estados = set()
    alfabeto = set() 
    transicoes = {}    
    estado_inicial = None 
    estados_aceitacao = set()

    for linha in linhas: #Le linha por linha
        linha = linha.strip()
        if linha.startswith('Q:'): #Primeira linha para os estados
            partes = linha.split()[1:] 
            estados = set(partes) #Cria um conjunto para os estados
        elif linha.startswith('I:'): #Segunda linha para estado inicial
            estado_inicial = linha.split()[1] 
        elif linha.startswith('F:'): #Terceira linha para estado final
            finais = linha.split()[1:] 
            estados_aceitacao = set(finais)
        elif '->' in linha: #Le as transicoes
            src, rest = linha.split('->') #divide a linha em duas partes a partir de '->' e coloca a primeira parte em src e a segunda em rest 
            src = src.strip()
            dst, simbolos = rest.split('|')
            dst = dst.strip()
            simbolos = simbolos.strip().split()
            for simbolo in simbolos:
                transicoes[(src, simbolo)] = dst
                alfabeto.add(simbolo)
        elif linha == '---':
            break

    return AFD(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)



