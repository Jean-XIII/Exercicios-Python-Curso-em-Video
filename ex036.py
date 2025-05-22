#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o emprestimo será negado.

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanto você ganha? '))
anos = int(input('Em quantos anos você pretende pagar? '))

meses = anos * 12
valor_prestacao = valor_casa / meses
percent_prestacao = salario * 30 / 100

if valor_prestacao < percent_prestacao:
    print('O emprestimo será concedido')
else:
    print('O emprestimo não será concedido')
