#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela: abaixo de 18,5, abaixo do peso; entre 18,5 e 25, peso ideal; 25 até 30, sobrepeso; 30 até 40, obesidade; acima de 40, obesidade mórbida.

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

calculo = peso / (altura ** 2)

if calculo < 18.5:
    print(f'Você tem o IMC de {calculo:.2f}, você está abaixo do peso')
elif 18.5 <= calculo < 25:
    print(f'Você tem o IMC de {calculo:.2f}, você está no peso ideal')
elif 25 <= calculo <= 30:
    print(f'Você tem o IMC de {calculo:.2f}, você está com sobrepeso')
elif 30 <= calculo <= 40:
    print(f'Você tem o IMC de {calculo:.2f}, você está com obesidade')
else:
    print(f'Você tem o imc de {calculo:.2f}, você está com obesidade morbida')
