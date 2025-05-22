#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: '))

if salario > 1250:
    aumento = salario * 10 / 100
else:
    aumento = salario * 15 / 100

print(f'Seu aumento com o salário atual de R${salario:.2f} será de {aumento:.2f}. Valor final: {aumento + salario}')
