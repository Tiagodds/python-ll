class pessoa:
    def __init__(self, nome, sexo, altura, peso):
        self.nome = nome
        self.sexo = sexo
        self.altura = altura
        self.peso = peso


lista_pessoas = []
quantidade = int(input('Digite a quantidade de cadastro que ira fazer: '))

for i in range(1, quantidade + 1):
    nome = pessoa(input('Nome: '))
    sexo = pessoa(nome, input('Sexo:' ))
    altura = pessoa(nome, sexo, input('Altura: '))
    peso = pessoa(nome, sexo, altura, input('Peso: '))
    