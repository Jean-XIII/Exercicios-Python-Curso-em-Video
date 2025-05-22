#Crie um programa que faça o computador jogar Jokenpô com você.

import random

escolha = input('Escreva se você quer pedra, papel ou tesoura: ').lower()

escolha_pc = random.choice(['pedra', 'papel', 'tesoura'])

if escolha == escolha_pc:
    print('Empate')
elif escolha == 'pedra' and escolha_pc == 'tesoura':
    print(f'Você ganhou! Você escolheu {escolha} e o computador escolheu {escolha_pc}')
elif escolha == 'pedra' and escolha_pc == 'papel':
    print(f'Você perdeu! Você escolheu {escolha} e o computador escolheu {escolha_pc}')
elif escolha == 'tesoura' and escolha_pc == 'papel':
    print(f'Você venceu! Você escolheu {escolha} e o computador escolheu {escolha_pc}')
elif escolha == 'tesoura' and escolha_pc == 'pedra':
    print(f'Você venceu! Você escolheu {escolha} e o computador escolheu {escolha_pc}')
elif escolha == 'papel' and escolha_pc == 'pedra':
    print(f'Você venceu! Você escolheu {escolha} e o computador escolheu {escolha_pc}')
elif escolha == 'papel' and escolha_pc == 'tesoura':
    print(f'Você perdeu! Você escolheu {escolha} e o computador escolheu {escolha_pc}')
