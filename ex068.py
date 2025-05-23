#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

cont = 0

while True:
    pc = randint(0, 11)
    numero = int(input('Digite um número: '))
    escolha = int(input('Digite 0 para par e 1 para ímpar: '))
    soma = pc + numero
    if soma % 2 == 0 and escolha == 0 or soma % 2 == 1 and escolha == 1:
        print('Você venceu!')
        cont += 1
    else:
        print(f'Você perdeu! O computador jogou {pc} e você {numero}, resultado: {soma}')
        break

print(f'Você venceu {cont} vezes')
