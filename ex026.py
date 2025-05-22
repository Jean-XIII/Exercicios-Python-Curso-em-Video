#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece pela primeira vez.
#Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').lower()

print(f'A letra "A" aparece {frase.count('a')}')
print(f'A letra "A" aparece pela primeira vez na posição {frase.find('a')+1}')
print(f'A letra "A" aparece pela última na posição {frase.rfind('a')+1}')
