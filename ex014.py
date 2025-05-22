#Escreva um programa que converta uma temperatura digitada °C e converta para °F.

temperatura = float(input('Digite a temperatura: '))

conversao = (temperatura * 9/5) + 32

print(f'{temperatura} °C em fareheint são {conversao:.2f} °F')
