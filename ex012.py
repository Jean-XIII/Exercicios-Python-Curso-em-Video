#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: '))

desconto = preco*5/100
novo_preco = preco - desconto

print(f'O novo preço é {novo_preco:.2f}')
