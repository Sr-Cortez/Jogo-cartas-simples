import random

class Baralho:
    
    def __init__(self):
        self._lista_cartas = []
        self._criar_cartas();

    def _criar_cartas(self):
        # @todo
        pass

    def adicionar_carta(self, c):
        self._lista_cartas.append(c)
    
    def retirar_carta(self):
        self._lista_cartas.pop(0)

    def embaralhar_cartas(self):
        random.shuffle(self._lista_cartas)

    def quantidade(self):
        return len(self._lista_cartas)


