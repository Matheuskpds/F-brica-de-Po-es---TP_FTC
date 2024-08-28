class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao
        print("Estados: ", self.estados)
        print("Alfabeto: ", self.alfabeto)
        print("Transicoes: ", self.transicoes)
        print("Estado inicial: ", self.estado_inicial)
        print("Estados de aceitacao: ", self.estados_aceitacao)
    
    def transicao(self, estado, simbolo):
        print("Transicao de ", estado, " com ", simbolo)
        return self.transicoes.get((estado, simbolo), None)
    
    def processar_input(self):
        estado = self.estado_inicial # Estado atual, começa como o inicial

        resposta = 's' # Variavel para a resposta de inserir mais um ingrediente ou nao
        while True:
            if resposta == 's':
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
    print("Lendo arquivo ", caminho_do_arquivo)
    with open(caminho_do_arquivo, 'r') as arq:
        linhas = arq.readlines()
    
    estados = set() #cria um conjunto vazio
    alfabeto = set()    #cria um conjunto vazio
    transicoes = {}    
    estado_inicial = None 
    estados_aceitacao = set()

    for linha in linhas:
        linha = linha.strip()
        if linha.startswith('Q:'):
            partes = linha.split()[1:] #separa a linha em partes e ignora o primeiro elemento (Q:)
            estados = set(partes) #cria um conjunto com os elementos de partes
        elif linha.startswith('I:'):
            estado_inicial = linha.split()[1] #pega o segundo elemento da linha
        elif linha.startswith('F:'):
            finais = linha.split()[1:] #pega o segundo elemento da linha
            estados_aceitacao = set(finais)
        elif '->' in linha:
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



