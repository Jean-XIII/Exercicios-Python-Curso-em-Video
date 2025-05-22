#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando a flag).

numero = cont = soma = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero

print(f'Foram digitados {cont - 1} números, a soma entre eles é {soma-999}')
