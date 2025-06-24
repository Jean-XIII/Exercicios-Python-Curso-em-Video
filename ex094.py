#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:  quantas pessoas cadastradas; A média de idade. Uma lista com mulheres; Uma lista com idade acima da média.

dicionario = {}
lista = []
mulheres = []
acima_media = []
soma = media = 0

while True:
    nome = input('Digite seu nome: ').capitalize()
    dicionario['nome'] = nome
    sexo = input('Informe seu sexo [M/F]: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite apenas M ou F: ').upper()
    dicionario['sexo'] = sexo
    idade = int(input('Digite sua idade: '))
    soma += idade
    dicionario['idade'] =idade
    lista.append(dicionario.copy())
    if sexo == 'F':
        mulheres.append(dicionario.copy())

    escolha = input('Você quer cadastrar mais pessoas [S/N]? ').upper()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break

print(f'Foram cadastradas {len(lista)} pessoas')
  
media = soma / len(lista)
print(f'A média de idade é {media}')

for pessoa in lista:
    if pessoa['idade'] > media:
        acima_media.append(pessoa)
print(f'As mulheres são {mulheres}')
print(f'Pessoas com idade acima da média: {acima_media}')
