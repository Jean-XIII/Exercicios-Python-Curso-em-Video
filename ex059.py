#Crie um programa que leia dois valores e mostre um menu como a seguir: [1] Somar; [2] Multiplicar; [3] Maior; [4]Novos números; [5]Sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

condicao = True
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

while condicao:
    escolha = int(input('Digite um número para escolher uma das opções a seguir:\n1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos números\n5 - Sair do programa\n'))
    if escolha > 5 or escolha <1:
        continue
    if escolha == 1:
        soma = numero1 + numero2
        print(f'{numero1} + {numero2} = {soma}\n')
        continue
    elif escolha == 2:
        multiplicar = numero1 * numero2
        print(f'{numero1} x {numero2} = {multiplicar}\n')
        continue
    elif escolha == 3:
        if numero1 > numero2:
            print(f'O número {numero1} é maior que {numero2}\n')
            continue
        else:
            print(f'O número {numero2} é maior que {numero1}\n')
            continue
    elif escolha == 4:
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
        continue
    else:
        condicao = False

print('Fim')

