#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dado = {}

dado['nome'] = input('Digite o nome do aluno: ').capitalize()
dado['media'] = float(input('Digite a média dele: '))

if dado['media'] < 5:
    dado['situacao'] = 'Reprovado'
elif dado['media'] >= 5 and dado['media'] < 7:
    dado['situacao'] = 'Recuperação'
else:
    dado['situacao'] = 'Aprovado'

for k, v in dado.items():
    print(f'{k} é igual a {v}')
