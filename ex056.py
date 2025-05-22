#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo; Quantas mulheres têm menos de 20 anos; Qual o nome do homem mais velho.

soma_idade = 0
soma_mulheres_menor = 0
h_mais_velho = ''
idade_mais_velho = 0

for c in range(0,4):
    nome = input('Digite seu nome: ').capitalize()
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual o seu sexo (M/F)? ').upper()
    soma_idade += idade
    if sexo == 'F' and idade < 20:
        soma_mulheres_menor += 1
    if sexo == 'M':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            h_mais_velho = nome

print(f'A média de idade é de {soma_idade / 4} anos')
print(f'{soma_mulheres_menor} mulheres tem menos de 20 anos')
print(f'O nome do homem mais velho é {h_mais_velho}')
