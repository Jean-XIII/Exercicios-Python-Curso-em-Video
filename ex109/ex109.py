#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

preco = float(input('Digite o preço: R$'))
print(f'Aumentando 13%, temos {moeda.aumentar(preco, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(preco)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco,True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco)}')
