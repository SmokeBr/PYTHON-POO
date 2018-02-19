class Veiculo:
    def __init__(self):
        self.cor = "Branco"
        self.velocidade = 0
        self.numero_rodas = 0

    def aumentar_velocidade(self, velocidade):
        self.velocidade += velocidade
        print("Rodando a %s km/h " %self.velocidade)

    def parar(self):
        self.velocidade = 0
        print("Parado !!! ")

    def buzinar(self):
        print("Biiii Biiii ")

class Bicicleta(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.numero_rodas = 2

    def buzinar(self):
        print("Triiim Triiim")

class Carro(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self.numero_rodas = 4

Ferrari = Carro()
chica = Bicicleta()
rosinha = Bicicleta()
