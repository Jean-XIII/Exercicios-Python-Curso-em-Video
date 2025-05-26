#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_geral = []
lista_impar = []
lista_par = []

while True:
    lista_geral.append(int(input('Digite um número: ')))
    escolha = input('Você quer continuar [S/N]? ').upper()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break
    
pos = 0
for numero in lista_geral:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    pos += 1

print(f'Lista geral: {lista_geral}')
print(f'Lista par: {lista_par}')
print(f'Lista ímpar: {lista_impar}')
