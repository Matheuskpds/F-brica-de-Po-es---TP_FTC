class APD:
    def __init__(self, estado_inicial, estado_final, transicoes):
        self.estado_atual = estado_inicial
        self.estado_final = estado_final
        self.transicoes = transicoes  # Dicionário de transições
        self.pilha = []

    def transicao(self, simbolo):
        # Verifica se há uma transição válida para o estado atual e símbolo de entrada
        if (self.estado_atual, simbolo) in self.transicoes:
            prox_estado, desempilha, empilha = self.transicoes[(self.estado_atual, simbolo)]
            
            # Verifica se o desempilha corresponde ao topo da pilha
            if desempilha == "" or (len(self.pilha) > 0 and self.pilha[-1] == desempilha):
                if desempilha != "":
                    self.pilha.pop()  # Desempilha o topo
                if empilha != "":
                    self.pilha.append(empilha)  # Empilha o novo símbolo
                
                # Muda para o próximo estado
                self.estado_atual = prox_estado
            else:
                self.estado_atual = "rejeita"
        else:
            self.estado_atual = "rejeita"

    def processar(self, entrada):
        # Processa a cadeia de entrada
        for simbolo in entrada:
            self.transicao(simbolo)
            if self.estado_atual == "rejeita":
                return False

        # Verifica se o estado final foi alcançado e a pilha está vazia
        return self.estado_atual == self.estado_final and len(self.pilha) == 0

def ler_arquivo_apd(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.read().strip().splitlines()

    # Processa as informações do arquivo
    estados = linhas[0].split(":")[1].strip().split()
    estado_inicial = linhas[1].split(":")[1].strip()
    estado_final = linhas[2].split(":")[1].strip()
    
    transicoes = {}

    for linha in linhas[3:]:
        if "->" in linha:
            partes = linha.split("|")
            estado_atual, proximo_estado = partes[0].split("->")
            estado_atual = estado_atual.strip()
            proximo_estado = proximo_estado.strip()
            simbolo_entrada = partes[1].strip()
            desempilha = partes[2].strip()
            empilha = partes[3].strip()
            
            # Adiciona a transição ao dicionário
            transicoes[(estado_atual, simbolo_entrada)] = (proximo_estado, desempilha, empilha)

    return APD(estado_inicial, estado_final, transicoes)

# Exemplo de uso:
arquivo_apd = "ap.txt"  # Nome do arquivo que contém o APD
apd = ler_arquivo_apd(arquivo_apd)

# Testando o APD com uma cadeia
cadeia = "aplfg"
resultado = apd.processar(cadeia)
print(f"Cadeia '{cadeia}' é aceita? {resultado}")