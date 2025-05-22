#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - equilátero, todos os lados são iguais; isósceles, dois lados iguais; escaleno, todos os lados diferentes.

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digte o compreimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível formar um triângulo')
    if reta1 == reta2 == reta3:
        print('O triângulo é equilátero')
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Não é possível formar um triângulo')
