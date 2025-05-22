#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
total = 0
for cont in range(1, numero + 1):
    if numero % cont == 0:
        total += 1

if total == 2:
    print(f'{numero} é primo')
else:
    print(f'{numero} não é primo')
