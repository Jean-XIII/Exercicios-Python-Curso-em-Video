#Faça um programa que tenha uma função chama maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print(f'O maior número entre {num} é {maior}')

maior(1, 50, 10, 13)