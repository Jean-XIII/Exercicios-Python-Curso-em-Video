#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Esse número já foi adicionado anteriormente')
    escolha = input('Quer continuar [S/N]? ').upper()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break

lista.sort()
print(lista)
