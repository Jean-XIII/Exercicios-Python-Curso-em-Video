#Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#093 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
lista_jogadores = list()

while True:
    jogador['nome'] = input('Digite o nome do jogador: ').capitalize()
    jogador['partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols o {jogador['nome']} fez na {c+1}º partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols[:])
    lista_jogadores.append(jogador.copy())
    gols.clear()

    escolha = input('Você que cadastrar mais jogadores [S/N]? ').upper()
    while escolha not in 'SN':
        escolha = input('Digite apenas S ou N: ').upper()
    if escolha == 'N':
        break
    
for pessoa in lista_jogadores:
    print(pessoa)
