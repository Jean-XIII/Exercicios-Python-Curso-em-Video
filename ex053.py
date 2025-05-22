#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ')
contrario = ''
frase_sem_espaco = ''

for i in range(0, len(frase)):
    if frase[i] != ' ':
        frase_sem_espaco += frase[i]

for i in range(len(frase) - 1, -1, -1):
    if frase[i] != ' ':
        contrario += frase[i]
print(frase_sem_espaco)
print(contrario)
if frase_sem_espaco == contrario:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
