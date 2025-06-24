#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: Quantas pessoas foram cadastradas; Uma listagem com as pessoas mais pesadas; Uma listagem com as pessoas mais leves.

lista_geral = []
lista_pesado = []
lista_leve = []

cadastradas = 0

while True:
    lista_geral.append(input('Digite seu nome: ').capitalize())
    lista_geral.append(int(input('Digite seu peso: ')))
    cadastradas += 1
    if cadastradas == 1:
        lista_pesado.append(lista_geral[:])
        lista_leve.append(lista_geral[:])
    else:
        if lista_geral[1] > lista_pesado[0][1]:
            lista_pesado.clear()
            lista_pesado.append(lista_geral[:])
        elif lista_geral[1] == lista_pesado[0][1]:
            lista_pesado.append(lista_geral[:])
        elif lista_geral[1] < lista_leve[0][1]:
            lista_leve.clear()
            lista_leve.append(lista_geral[:])
        elif lista_geral[1] == lista_leve[0][1]:
            lista_leve.append(lista_geral[:])
    lista_geral.clear()

    escolha = input('Você quer continuar [S/N]? ').upper()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break

print(f'Foram cadastradas {cadastradas} pessoas')
print('As pessoas mais pesadas são ', end = '')
for pessoa in lista_pesado:
    print(f'{pessoa[0]}, pesando {pessoa[1]}, ', end = '')
print('\nAs pessoas mais leves são ', end = '')
for pessoa in lista_leve:
    print(f'{pessoa[0]}, pesando {pessoa[1]}, ', end = '')

