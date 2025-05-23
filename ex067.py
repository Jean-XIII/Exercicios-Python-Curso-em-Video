#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    for c in range(0, 11):
        print(f'{c} + {numero} = {c + numero}')
        if c == 10:
            continue
