#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = int(input('Qual a distância da viagem? '))

viagem_curta = distancia * 0.5
viagem_longa = distancia * 0.45

if distancia > 200:
    print(f'Uma viagem de {distancia}Km custará R${viagem_longa:.2f}')
else:
    print(f'Uma viagem de {distancia}Km custará R${viagem_curta:.2f}')
