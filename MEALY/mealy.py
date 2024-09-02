class Mealy:
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
        print("Alfabeto de saída: ", self.alfabeto_saida)
        print("Transições: ", self.transicoes)
        print("Reacoes: ", self.reacoes)
  
    def transicao(self, estado, simbolo):
        print("Transição de ", estado, " com ", simbolo)
        return self.transicoes.get((estado, simbolo), (None, None))

    def processar_input_mealy(self):
        estado = self.estado_inicial  # Estado atual, começa como o inicial

        resposta = 's'  # Variável para a resposta de inserir mais um ingrediente ou não
        while True:
            if resposta == 's':
                simbolo = input("\nQual ingrediente será inserido:\n")
                
                print("\nEstado atual: ", estado)
                print("Símbolo atual: ", simbolo)
                estado, saida = self.transicao(estado, simbolo)  # Realiza a transição dos estados

                if estado is None:
                    print("Transição inválida!")
                    break

                reac = self.reacoes[saida]
                print(reac)
                #print("Saída: ", saida)
            elif resposta == 'n':
                break
            else:
                print("Resposta inválida!")
            resposta = input("\nDeseja inserir mais um ingrediente(s/n)?\n")
            resposta = resposta.strip()
       
        print("\nEstado final: ", estado)
        return

def ler_arquivo_mealy(caminho_do_arquivo):
    print("Lendo arquivo ", caminho_do_arquivo)
    with open(caminho_do_arquivo, 'r') as arq:
        linhas = arq.readlines()
    
    estados = set()  # Conjunto vazio para os estados
    alfabeto = set()  # Conjunto vazio para o alfabeto
    reacoes = {}
    alfabeto_saida = set()
    transicoes = {}

    for linha in linhas:
        linha = linha.strip()
        if linha.startswith('Q:'):
            est = linha.split()[1:]  # Pega os estados
            estados.update(est)
        elif linha.startswith('I:'):
            estado_inicial = linha.split()[1]  # Pega o segundo elemento da linha
        elif '=' in linha:
            simbolo, reacao = linha.split('=')
            simbolo = simbolo.strip()
            reacao = reacao.strip()
            reacoes[simbolo] = reacao
        elif '->' in linha:
            src, rest = linha.split('->')  # Divide a linha em duas partes a partir de '->'
            src = src.strip()
            dst, simbolos = rest.split('|')
            dst = dst.strip()
            simbolos = simbolos.strip().split()
            for simbolo in simbolos:
                simbolo_entrada, saida = simbolo.split('/')
                transicoes[(src, simbolo_entrada)] = (dst, saida)
                alfabeto.add(simbolo_entrada)
                alfabeto_saida.add(saida)
        elif linha == '---':
            break

    return Mealy(estados, estado_inicial, alfabeto, alfabeto_saida, transicoes, reacoes)