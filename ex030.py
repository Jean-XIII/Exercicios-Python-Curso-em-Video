#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Digite o número: '))
resultado = numero % 2

if resultado == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')
