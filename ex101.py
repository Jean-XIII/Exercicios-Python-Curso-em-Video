#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(n):
    if n < 16:
        return 'NEGADO'
    elif 16 <= n < 18:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'
    
nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2025 - nascimento

print(f'Com {idade} anos seu voto é {voto(idade)}')
