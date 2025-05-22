#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - para binário, 2 - para octal, 3 - para hexadecimal.

numero = int(input('Digite um número: '))
escolha = int(input('Escolha um número para iniciar a conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))

if escolha == 1:
    print(f'O número {numero} convetida para binário é {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O número {numero} convertido para octal é {oct(numero)[2:]}')
else:
    print(f'O número {numero} convertido para hexadecimal é {hex(numero)[2:]}')
