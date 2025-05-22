#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi maior e o menor peso lidos.

maior = menor = 0

for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if c == 0:
        maior = menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O menor peso foi {menor}, e o maior foi {maior}')
