#Incompleto
#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista completa. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
lista_geral = []
cont = 0

while True:
    nome = input('Insira o nome do aluno: ').capitalize()
    lista.append(nome)
    nota1 = float(input('Insira a primeira nota: '))
    lista.append(nota1)
    nota2 = float(input('Insira a segunda nota: '))
    lista.append(nota2)
    lista_geral.append(lista[:])
    lista.clear()

    escolha = input('Você quer continuar [S/N]? ').upper()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break

for aluno in lista_geral:
    media = (aluno[1] + aluno[2])/2
    print(f'A média do aluno {aluno[0]} é {media}')

while True:
    indiv = input('Escreva o nome do aluno que você quer ver as notas: ').capitalize()
    for aluno in lista_geral:
        if indiv == aluno[0]:
            print(f'As notas do {aluno[0]} são {aluno[1]} e {aluno[2]}')
            cont += 1
        
    if cont >= len(lista_geral):
        print(f'O aluno {indiv} não se encontra na lista')
        break
