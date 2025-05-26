#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: Quantas vezes apareceu o valor 9; Em que posição foi digitado o primeiro valor 3; Quais foram os números pares.

cont = 0

numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

print(f'O número 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor foi 3 digitado na posição {numeros.index(3)+1}')
else:
    print('O número 3 não está na tupla')

for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(f'O número {numeros[c]} é par', end= ', ')
        cont = 1
if cont == 0 :
    print('Não há números pares')
