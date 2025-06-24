#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dicionario = {}
lista = []
tot_gols = 0

dicionario['nome'] = input('Digite o nome do jogador: ').capitalize()
qtd_partidas = int(input('Digite quantas partidas foram jogadas: '))

for c in range(0, qtd_partidas):
    gols = int(input(f'Digite a quantidade de gols que o {dicionario["nome"]} fez na partida {c+1}º: '))
    tot_gols += gols
    lista.append(gols)
dicionario['gols'] = lista[:]
dicionario['total'] = tot_gols

print(dicionario)

for k, v in dicionario.items():
    print(f'O campo {k} tem valor {v}')

print(f'O jogador {dicionario['nome']} jogou {qtd_partidas}')
for c in range(0, qtd_partidas):
    print(f'Na partida {c+1}, fez {dicionario["gols"][c]} gols')
