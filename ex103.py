#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(n = '<desconhecido>', g = 0):
    print(f'O jogador {n} fez {g} gols.')
    
nome = input('Digite o nome do jogador: ').capitalize()
gols = input('Número de gols: ')

if nome == '':
    ficha(g = gols)
else:
    ficha(nome, gols)
