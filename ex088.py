#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para jogo, cadastrando tudo em uma lista composta.

from random import randint

lista = []
lista_total = []
cont = 0

jogos = int(input('Quantos jogos serão jogados? '))

while cont < jogos:
    for j in range(0, 6):
        numero = randint(1, 60)
        lista.append(numero)
    lista_total.append(lista[:])
    lista.clear()
    cont += 1


for lista in lista_total:
    lista.sort()
    print(lista)
