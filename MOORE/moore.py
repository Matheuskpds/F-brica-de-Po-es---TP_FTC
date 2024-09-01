def ler_arquivo_moore(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.read().strip().splitlines()

    print("Linhas do arquivo:", linhas)  # Mensagem de depuração

    if len(linhas) < 5:
        raise ValueError("O arquivo de entrada está no formato incorreto.")

    # Ler conjunto de estados
    estados = linhas[0].split(':')[1].strip().split()
    
    # Ler símbolos de entrada
    simbolos_entrada = linhas[1].split(':')[1].strip().split()
    
    # Ler símbolos de saída
    simbolos_saida = linhas[2].split(':')[1].strip().split()
    
    # Ler funções de saída
    funcao_saida = {}
    for linha in linhas[4:4 + len(estados)]:
        if ':' not in linha:
            print(f"Erro na linha de saída: {linha}")  # Mensagem de erro
            raise ValueError(f"Linha mal formatada para função de saída: {linha}")
        estado, saida = linha.split(':')
        funcao_saida[estado.strip()] = saida.strip()
    
    # Ler funções de transição
    transicoes = {}
    for linha in linhas[4 + len(estados):]:
        if '->' not in linha:
            print(f"Erro na linha de transição: {linha}")  # Mensagem de erro
            raise ValueError(f"Linha mal formatada para transição: {linha}")
        estado_atual, resto = linha.split('->')
        estado_atual = estado_atual.strip()
        partes = resto.split('|')
        if len(partes) < 2:
            print(f"Erro na linha de transição: {linha}")  # Mensagem de erro
            raise ValueError(f"Linha mal formatada para transição: {linha}")
        proximo_estado = partes[0].strip()
        simbolo_entrada = partes[1].strip()
        transicoes[(estado_atual, simbolo_entrada)] = proximo_estado
    
    return estados, simbolos_entrada, simbolos_saida, funcao_saida, transicoes

class MoorePotionMachine:
    def __init__(self, estados, simbolos_entrada, simbolos_saida, funcao_saida, transicoes):
        self.states = estados
        self.symbols = simbolos_entrada
        self.outputs = funcao_saida
        self.transitions = transicoes
        self.initial_state = estados[0]
        self.current_state = self.initial_state

    def process_input(self, input_string):
        output = []
        for symbol in input_string:
            if (self.current_state, symbol) in self.transitions:
                self.current_state = self.transitions[(self.current_state, symbol)]
                output.append(self.outputs[self.current_state])
            else:
                output.append("Erro: Transição não encontrada")
        return ' -> '.join(output)

def main():
    arquivo = 'moore.txt'  # Nome do arquivo de entrada
    estados, simbolos_entrada, simbolos_saida, funcao_saida, transicoes = ler_arquivo_moore(arquivo)

    # Criar a máquina
    machine = MoorePotionMachine(estados, simbolos_entrada, simbolos_saida, funcao_saida, transicoes)

    # Obter entrada do usuário
    input_string = input("Digite a sequência de ingredientes (usando os símbolos disponíveis): ")
    
    # Processar a entrada e exibir o resultado
    output = machine.process_input(input_string)
    print(f"Saída para a entrada '{input_string}': {output}")

if __name__ == "__main__":
    main()