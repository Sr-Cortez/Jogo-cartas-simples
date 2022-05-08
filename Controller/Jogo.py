from Model.Baralho import Baralho
from View.Tela import Tela

class Jogo:

    def __init__(self):
        self._lista_jogadores = []
        self._baralho = Baralho()
        self._programa = Tela() 

    def iniciar(self):
        self.adicionar_jogadores()
        self.iniciar_rodadas()
        self.analisar_resultado()

    def iniciar_rodadas(self):

        #@todo
        pass
    
    def adicionar_jogadores(self):
        #@todo
        pass

    def analisar_resultado(self):
        #@todo
        pass
