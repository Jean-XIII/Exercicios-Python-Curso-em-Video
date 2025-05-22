#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu  preço normal e condição de pagamento: - à vista dinheiro/ cheque, 10% de desconto; - em até 2X no cartão, preço normal; 3X ou mais no cartão, 20% de juros; - à vista no cartão, 5% de desconto.

preco = float(input('Digite o preço: R$'))
escolha = int(input('Digite 1 para pagamento à vista/cheque\nDigite 2 para pagamento à vista no cartão\nDigite 3 para pagamento à 2X no cartão\nDigite 4 para pagamento à 3X ou mais no cartão\n'))

if escolha == 1:
    calculo = preco + (preco * 10 / 100)
    print(f'Preço final: R${calculo:.2f}')
elif escolha == 2:
    calculo = preco - (preco * 5 / 100)
    print(f'Preço final: R${calculo:.2f}')
elif escolha == 4:
    calculo = preco + (preco * 20 / 100)
    print(f'Preço final: R${calculo:.2f}')
