#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

condicao = ''
cont = soma = maior = menor = 0

while condicao != 'N':
    numero = int(input('Digite um número: '))
    if maior == 0 and menor == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    cont += 1
    soma += numero
    condicao = input('Quer digitar outro número [S/N]? ').upper()
    while condicao != 'S' and condicao != 'N':
        condicao = input('Digite apenas S ou N: ').upper()

media = soma / cont

print(f'A média é {media}')    
print(f'O maior número é {maior} e o menor é {menor}')
