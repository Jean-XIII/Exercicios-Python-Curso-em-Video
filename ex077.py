#Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('um', 'dois', 'tres', 'quatro', 'cinco')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in tupla:
    print(f'A palavra {palavra} tem como vogal ', end = '')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end='')
    print('')
