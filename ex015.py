#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite os Km percorridos: '))
dias = int(input('Digite por quantos dias ele foi alugado: '))

preco_dias = dias * 60
preco_km = km * 0.15
preco_final = preco_km + preco_dias

print(f'{dias} dias de aluguel do carro equivalem a R${preco_dias:.2f}, e {km}Km equivalem a R${preco_km:.2f}.\n Preço final: R${preco_final:.2f}')
