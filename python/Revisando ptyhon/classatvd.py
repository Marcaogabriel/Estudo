# Um carro tem: Marca, Velocidade tem e cor
# Ações com um carro: Ligar, Desligar e ler manual de informações

class Carro:
    def __init__(self, marca, velocidade, cor):
        self.marca = marca
        self.velocidade = velocidade
        self.cor = cor

    def Ligar(self):
        print('Girando a chave \r Ligando o carro')

    def Desligar(self):
        print('Girando a chave \r Desligando carro')

    def Manual(self):
        print(f'A marca do carro é {self.marca} a velocidade maxíma {self.velocidade} e a sua cor é {self.cor}')

carro1 = Carro('Porshe', '160kg', 'Braco')
carro1.Ligar()
carro1.Desligar()
carro1.Manual()