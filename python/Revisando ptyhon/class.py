# class
# syntaxe
# Coisas que um computador tem : Marca, mémoria ram, placa de video


class computador:
    def __init__(self, marca, memoria_ram, placa_de_video): # o init -> é chamado de consultor e permite criar a funcionalidade da class
        self.marca = marca # self -> Propriedades
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou Desligando')

    def Exibirconfigurações(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)


computador1 = computador('Asus','8gb','Nvideo')
#computador1.Ligar()
#computador1.Desligar()
#computador1.Exibirconfigurações()
computador1.marca()
