#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

ranking = {}
dicionario = {}

for c in range(0, 4):
    dicionario[f'jogador{c+1}'] = randint(1, 6)

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)

for jogador in ranking:
    print(jogador)
