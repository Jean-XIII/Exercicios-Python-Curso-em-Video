#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

numero = float(input('Digite um número real: '))

print(f'A parte inteira de {numero} é {math.trunc(numero)}')
