#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - até 9 anos, mirim; - até 14 anos, infantil; - até 19 anos, junior; até 25 anos, senior; -acima, master.

nascimento = int(input('Digite o seu ano de nascimento: '))

calculo = 2025 - nascimento

if calculo <= 9:
    print('Você é mirim')
elif 9 < calculo <= 14:
    print('Você é infantil')
elif 14 < calculo <= 19:
    print('Você é junior')
elif 19 < calculo <= 25:
    print('Você é sênior')
else:
    print('Você é master')
