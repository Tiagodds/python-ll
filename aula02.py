# saldo = 100
# resposta = True

# while saldo != 0:
#     print("Saldo:", saldo)
#     saque = int(input('Valor de Saque: '))
#     saque =+ saque
#     if saque > saldo:
#         print('Valor mais alto que o disponivel')
#         break
#     saldo = saldo - saque
    
       



import random
#FOR 
    
nume_secreto = random.randint(1,100)

total_tent = 3


for rodada in range (1, total_tent + 1):
    print(f'Tentativa: {rodada:02d} de {total_tent:02d}')

    Tentativa= int(input('Tente acertar o número de 1 a 100: '))
    print('Você digitou: ',Tentativa)

    if Tentativa < nume_secreto:
        print('É Numero mais alto')
    else:
        print('É um número mais baixo')

    # if Tentativa < 1 or Tentativa > 100:
        # print('tentativa inválida! Somente números de 1 a 100!')
        


    acerto = Tentativa == nume_secreto

    if acerto:
        print("Parabéns, você acertou")
        break

    else:
        print('Que pena, não foi dessa vez')




#PROGRAMAÇÃO ORIENTADA A OBJETOS
        
# 1° EXISTE PARA CRIAR PARTE DE CÓDIGOS PARA QUE POSSA SER REUTILIZADO - PADRÕES PARA O CÓDIGO

# MVC - MODEL, VIEW, CONTROLE
        
# CLASSE - REPRESENTA ALGO REAL  CARACTERISTICAS E AÇÕES 
        
# 