#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: Qual é o total gasto na compra; Quantos produtos custam mais de R$1000; Qual é o nome do produto mais barato.

preco_final = p1000 = preco_b = 0
p_barato = ''

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    escolha = input('Você quer continuar [S/N]? ').upper()

    preco_final += preco

    if preco > 1000:
        p1000 += 1
    if preco_b == 0:
        preco_b = preco
        p_barato = nome
    elif preco < preco_b:
        preco_b = preco
        p_barato = nome

    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break

print(f'Preço final: R${preco_final:.2f}\n{p1000} produtos custam mais de R$1000\nO produto mais barato é o {p_barato}, custando R${preco_b:.2f}')
