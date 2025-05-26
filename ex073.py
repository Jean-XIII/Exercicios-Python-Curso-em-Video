#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: Os 5 primeiros; Os últimos 4 colocados; Times em ordem alfabética; Em que posição está o time da Chapecoense.

tupla = ('e', 'd', 'c', 'b', 'a', 'chapecoense', 'g', 'h', 'i', 'j',)

print(f'Os cinco primeiros colocados são: {tupla[:5]}')
print(f'Os últimos 4 colocados são: {tupla[-4:]}')
print(f'Em ordem alfabética: {sorted(tupla)}')
print(f'Chapecoense está na posição {tupla.index('chapecoense')+1}')
