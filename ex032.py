#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano: '))

calculo = ano % 4

if calculo == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
