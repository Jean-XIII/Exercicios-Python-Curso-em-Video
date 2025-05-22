#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input('Digite o seu ano de nascimento: '))

ano_atual = 2025
calculo = ano_atual - nascimento

if calculo < 18:
    print(f'Ainda não chegou a hora de você se alistar, ainda faltam {18 - calculo} anos')
elif calculo == 18:
    print('Está na hora de você se alistar')
else:
    print(f'Já passou da hora de você se alistar. Já se passou {calculo - 18} anos')
