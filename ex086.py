#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for i in range(0,3):
    for j in range(0, 3):
        numero = int(input(f'Digite um número para a posição [{i}][{j}]: '))
        matriz[i].append(numero)

for c in range(0, 3):
    print(matriz[c])
