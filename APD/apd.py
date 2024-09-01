class APD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes  # Dicionário de transições
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao
        self.pilha = []
        print("Estados: ", self.estados)
        print("Alfabeto: ", self.alfabeto)
        print("Transicoes: ", self.transicoes)
        print("Estado inicial: ", self.estado_inicial)
        print("Estados de aceitacao: ", self.estados_aceitacao)

    def processar_input_apd(self):
        estado = self.estado_inicial  # Estado atual, começa como o inicial
        
        resposta = 's'
        while True:
            if resposta == 's':
                simbolo = input("\nQual ingrediente será inserido:\n")
                
                print("\nEstado atual: ", estado)
                print("Simbolo atual: ", simbolo)
                prox_estado, desempilha, empilha = self.transicoes.get((estado, simbolo), (None, None, None))
                if prox_estado is None:  # Caso não exista a transição, retorna falso
                    return False
                else:
                    # Verifica se o desempilha corresponde ao topo da pilha
                    if desempilha == "" or (len(self.pilha) >= len(desempilha) and self.pilha[-len(desempilha):] == list(desempilha)):
                        if desempilha != "":
                            # Desempilha cada caractere de desempilha
                            for _ in range(len(desempilha)):
                                self.pilha.pop()

                        if empilha != "":
                            # Empilha cada caractere de empilha
                            for char in empilha:
                                self.pilha.append(char)
                    
                        # Muda para o próximo estado
                        estado = prox_estado
                    else:
                        return False
            elif resposta == 'n':
                break
            else:
                print("Resposta inválida!")
            resposta = input("\nDeseja inserir mais um ingrediente(s/n)?\n")
            resposta = resposta.strip()
        print("\nEstado final: ", estado)
        if estado in self.estados_aceitacao and len(self.pilha) == 0: # Procura se o estado em que parou é um estado final
                return True
        else:
            return False
        
        
def ler_arquivo_apd(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.read().strip().splitlines()

    estados = set()  # Cria um conjunto vazio
    alfabeto = set()  # Cria um conjunto vazio
    transicoes = {}    
    estado_inicial = None 
    estados_aceitacao = set()
    
    for linha in linhas:
        linha = linha.strip()
        if linha.startswith('Q:'):
            partes = linha.split()[1:]  # Separa a linha em partes e ignora o primeiro elemento (Q:)
            estados = set(partes)  # Cria um conjunto com os elementos de partes
        elif linha.startswith('I:'):
            estado_inicial = linha.split()[1]  # Pega o segundo elemento da linha
        elif linha.startswith('F:'):
            finais = linha.split()[1:]  # Pega o segundo elemento da linha
            estados_aceitacao = set(finais)
        elif "->" in linha:
            partes = linha.split("|")
            estado_atual, proximo_estado = partes[0].split("->")
            estado_atual = estado_atual.strip()
            proximo_estado = proximo_estado.strip()
            simbolo_entrada = partes[1].strip()
            alfabeto.add(simbolo_entrada)
            desempilha = partes[2].strip()
            empilha = partes[3].strip()
            
            # Adiciona a transição ao dicionário
            transicoes[(estado_atual, simbolo_entrada)] = (proximo_estado, desempilha, empilha)
    
    return APD(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)