#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

random = randint(0, 5)

numero = int(input('Digite um número: '))
if random == numero:
    print(f'Você acertou! O computador escolheu o número {random} e você também.')
else:
    print(f'Você errou, o computador escolheu o número {random}.')
