#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco')

while True:
    numero = int(input('Digite um número entre 0 e 5: '))
    if numero < 0 or numero > 5:
        print('Número inválido')
    else:
        break

print(f'Você digitou o número {tupla[numero]}')
