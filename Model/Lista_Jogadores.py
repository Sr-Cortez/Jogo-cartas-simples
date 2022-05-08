

class ListaJogadores:

    def __init__(self):
        self._lista_jogadores = []

    def adicionar_jogador(self, j):
        self._lista_jogadores.append(j)

    def obter_proximo_jogador(self):
        # @todo
        pass

    def obter_lista_ordenada_pontos(self):
            return self._lista_jogadores.sort(key=lambda x: x.pontos)

