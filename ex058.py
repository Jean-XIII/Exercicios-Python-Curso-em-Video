#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

escolha_pc = randint(0, 10)
condicao = True
palpites = tentativa = 0
while condicao:
    tentativa = int(input('Escolha um número entre 0 e 10: '))
    if 0 > tentativa or tentativa > 10:
        continue
    palpites += 1
    if tentativa == escolha_pc:
        print(f'Você acertou! Foram feitas {palpites} tentativas')
        condicao = False
    else:
        print('Você errou, tente novamente')
