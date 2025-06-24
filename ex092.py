#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dado = {}

dado['nome'] = input('Digite seu nome: ').capitalize()
nascimento = int(input('Digite seu ano de nascimento: '))
dado['idade'] = 2025 - nascimento
dado['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dado['ctps'] != 0:
    dado['contratacao'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário: R$'))
    dado['aposentadoria'] = dado['idade'] + ((dado['contratacao'] + 35) - 2025)

for k, v in dado.items():
    print(f'{k} tem o valor {v}')
