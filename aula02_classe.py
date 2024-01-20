"""
    Caracteristicas  - comum para todos os objetos
        Cor
        Modelo

    
    Ações - o que o objeto pode fazer
        Andar 
        Parar
        Liga

    """


class Automovel:
    def __init__(self, cor, modelo, num_portas, tipo_cambio, placa, marca): #self controla quais são as caracteristicas
        self.cor = cor
        self.modelo = modelo 
        self.num_portas = num_portas
        self.tipo_cambio = tipo_cambio
        self.motor = False
        self.placa = placa
        self.marca = marca


def ligar(self):
    if (self.motor == True):
        print('Carro já esta ligado')
    else:
        self.motor = True




carro = Automovel("cinza", "350i", '4', "Automático","EXR-5289", "BMW")
print(carro.motor)
carro.ligar()
print(carro.motor)

