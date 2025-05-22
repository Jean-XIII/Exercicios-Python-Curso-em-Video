#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = int(input('Digite um número: '))
string = str(numero)

print(f'Unidade: {string[0]}')
print(f'Dezena: {string[1]}')
print(f'Centena: {string[2]}')
print(f'Milhar: {string[3]}')
