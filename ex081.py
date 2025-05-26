#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: Quantos números foram digitados; A lista de valores, ordenada de forma decrescente; Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    escolha = input('Você quer continuar [S/N]? ').upper()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break

print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
