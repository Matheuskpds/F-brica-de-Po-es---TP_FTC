class DFA:
    def __init__(self):
        self.states = {'I', 'A'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            ('I', 'a'): 'A',
            ('I', 'b'): 'I',
            ('A', 'a'): 'I',
            ('A', 'b'): 'A'
        }
        self.start_state = 'I'
        self.accept_states = {'I'}
    
    def transition(self, state, symbol):
        return self.transitions.get((state, symbol), None)
    
    def process_input(self, input_string):
        state = self.start_state
        for symbol in input_string:
            state = self.transition(state, symbol)
            if state is None:
                return False
        return state in self.accept_states


def leitura_arquivo():
    with open("/Fabrica_de_Pocoes-TP_FTC/afd.txt", "r") as file:
        linhas = file.readlines()
        print(linhas)


arquivo = leitura_arquivo()

"""
# Exemplo de uso
if __name__ == "__main__":
    dfa = DFA()
    
    input_string = input("Insira a string para verificar: ")
    if dfa.process_input(input_string):
        print("String aceita.")
    else:
        print("String rejeitada.")"""
