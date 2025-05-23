#Crie um programa que leia vários númeors inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando a flag).

cont = soma = numero = 0

while True:
    soma += numero
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    cont += 1

print(f'Foram digitados {cont} números e a soma deles é {soma}')
