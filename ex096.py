#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area = l * c
    print(area)

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno:'))

area(largura, comprimento)
