#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Quantos reais você tem? '))

dolar = reais / 5.7

print(f'Com R${reais:.2f}, você pode comprar ${dolar:.2f}.')
