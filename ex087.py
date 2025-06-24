#Aprimore o desafio anterior, mostrando no final: A soma de todos os valores pares digitados; A soma dos valores da terceira coluna; O maior valor da segunda linha.

matriz = [[], [], []]
par = t_coluna = maior_l = 0

for i in range(0, 3):
    for j in range(0, 3):
        numero = int(input(f'Digite um número para a posição [{i}][{j}]: '))
        matriz[i].append(numero)
        if numero % 2 == 0:
            par += numero

for lista in matriz:
    if lista[2]:
        t_coluna += lista[2]

for i in range(0, 3):
    for j in range(0, 3):
        if i == 1:
            if matriz[i][j] > maior_l:
                maior_l = matriz[i][j]
            

for c in range(0, 3):
    print(matriz[c])

print(f'A soma dos pares é {par}')
print(f'A soma dos valores da terceira coluna é {t_coluna}')
print(f'O maior valor da segunda linha é {maior_l}')
