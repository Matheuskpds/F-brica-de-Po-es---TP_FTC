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
    
    def processar_input(self, input_string):
        print("Processando input: ", input_string)
        estado = self.estado_inicial
        for simbolo in input_string:
            print("Estado atual: ", estado)
            print("Simbolo atual: ", simbolo)
            estado = self.transicao(estado, simbolo)
            if estado is None:
                return False
        print("Estado final: ", estado)
        return estado in self.estados_aceitacao

def ler_arquivo(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'r') as arq:
        linhas = arq.readlines()
    
    estados = set() #cria um conjunto vazio
    alfabeto = set()    #cria um conjunto vazio
    transicoes = {}    
    estado_inicial = None 
    estados_aceitacao = None

    for linha in linhas:
        linha = linha.strip()
        if linha.startswith('Q:'):
            partes = linha.split()[1:] #separa a linha em partes e ignora o primeiro elemento (Q:)
            estados = set(partes) #cria um conjunto com os elementos de partes
        elif linha.startswith('I:'):
            estado_inicial = linha.split()[1] #pega o segundo elemento da linha
        elif linha.startswith('F:'):
            estados_aceitacao = linha.split()[1] #pega o segundo elemento da linha
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

    return AFD(estados, alfabeto, transicoes, estado_inicial, {estados_aceitacao})

# Testar a máquina com a entrada "a p p"
afd = ler_arquivo("afd.txt")

# Defina a entrada para teste
entrada = ["a", "p", "p"]

# Processar a entrada
if afd.processar_input(entrada):
    print("String aceita.")
else:
    print("String rejeitada.")
