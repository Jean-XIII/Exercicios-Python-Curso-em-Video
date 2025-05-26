#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

maior = menor = 0

numeros = (randint(0, 13), randint(0, 13), randint(0, 13), randint(0, 13), randint(0, 13))

for c in range(0, len(numeros)):
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        elif numeros[c] < menor:
            menor = numeros[c]

print(f'Lista: {numeros}')
print(f'O maior número é {maior} e o menor é {menor}')
