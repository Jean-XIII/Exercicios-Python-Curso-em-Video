#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você vai pagar uma multa de R${multa:.2f}')
else:
    print('Você está na velocidade permitida')
