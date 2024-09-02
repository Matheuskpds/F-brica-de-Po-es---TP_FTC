class Moore:
    def __init__(self, estados, estado_inicial, alfabeto, alfabeto_saida, transicoes, reacoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.alfabeto_saida = alfabeto_saida
        self.reacoes = reacoes
        print("Estados: ", self.estados)
        print("Estado inicial: ", self.estado_inicial)
        print("Alfabeto: ", self.alfabeto)
        print("Alfabeto saida: ", self.alfabeto_saida)
        print("Transicoes: ", self.transicoes)
        print("Reacoes: ", self.reacoes)
  
    
    def transicao(self, estado, simbolo):
        print("Transicao de ", estado, " com ", simbolo)
        return self.transicoes.get((estado, simbolo), None)
    
    def processar_input_moore(self):
        estado = self.estado_inicial # Estado atual, começa como o inicial

        resposta = 's' # Variavel para a resposta de inserir mais um ingrediente ou nao
        while True:
            if resposta == 's':
                simbolo = input("\nQual ingrediente será inserido:\n")
                
                print("\nEstado atual: ", estado)
                print("Simbolo atual: ", simbolo)
                estado = self.transicao(estado, simbolo) # Realiza a transicao dos estados

                saida = self.estados[estado]
                reac = self.reacoes[saida]
                print(reac)
            elif resposta == 'n':
                break
            else:
                print("Resposta inválida!")
            resposta = input("\nDeseja inserir mais um ingrediente(s/n)?\n")
            resposta = resposta.strip()
       
        print("\nEstado final: ", estado)
        return

def ler_arquivo_moore(caminho_do_arquivo):
    print("Lendo arquivo ", caminho_do_arquivo)
    with open(caminho_do_arquivo, 'r') as arq:
        linhas = arq.readlines()
    
    estados = {} #cria um conjunto vazio
    alfabeto = set()    #cria um conjunto vazio
    reacoes = {}
    transicoes = {}

    for linha in linhas:
        linha = linha.strip()
        if linha.startswith('Q:'):
            est , saidas = linha.split('|') #separa a linha em partes e ignora o primeiro elemento (Q:)
            est = est.split()[1:]
            saidas = saidas.split()
            for i in range(0,len(est)):
                estados[est[i]] = saidas[i]
        elif linha.startswith('I:'):
            estado_inicial = linha.split()[1] #pega o segundo elemento da linha
        elif '=' in linha:
            simbolo, reacao = linha.split('=')
            simbolo = simbolo.strip()
            reacao = reacao.strip()
            reacoes[simbolo] = reacao
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

    return Moore(estados, estado_inicial, alfabeto, saidas, transicoes, reacoes)