# print('HELLO WORD.\nGOOD MORNING!!') 

# # PI variável todo em letra maiúscula é uma variável constante

# print('ola {}'.format(input('Qual o seu nome? ')+ '!'))

# print('Seja bem vindo a aulda de' + ' Python II')


# n1= int(input('Digite o 1° número: '))
# n2= int(input('Digite o 2° número: '))


# operação = str(input('Operações matemáticas!!!\n[A] Soma\n[B] Subtração\n[C] Multiplicação\n[D] Divisão\nQue operação matemática deseja fazer? 10')).upper()

# if operação == "A":
#     print(f'O resultado da soma entre {n1} e {n2} é {n1+n2}')
            

# elif operação == "B":
#     print(f'O resultado da subtração entre {n1} e {n2} é {n1-n2}')
            

# elif operação == "C":
#     print(f'O resultado da multiplicação entre {n1} e {n2} é {n1*n2}')
            

# elif operação == "D":
#     print(f'O resultado da divisão entre {n1} e {n2} é {n1/n2}')

# else:
#     print('Alternativa incorreta!!! Tente novamente')



    #PENSAMENTO COMPUTACIONAL 
    
        # DECOMPOSIÇÃO 
        # PADORES
        # ABSTRAÇÃO
        # ALGORITIMO
    

# 1
# Se a média for igual ou maior que 7 esta aprovado 6
# entre 4 a 6 recuperação 
# menor que 4 reprovação


n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
n3 = float(input('Digite a 3° nota: '))
n4 = float(input('Digite a 4° nota: '))

media = (n1+n2+n3+n4)/4

if media >= 7:
    print(f"Aprovado!sua nota foi {media}")
elif media >= 4:
    print(f"Recuperação, sua nota foi {media}")
else:
    print(f"Reprovado, sua nota foi {media}")



