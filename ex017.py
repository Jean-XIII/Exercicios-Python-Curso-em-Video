#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

#Forma 1 de se resolver:
hipotenusa_modulo = hypot(cat_oposto, cat_adjacente)

#Forma 2 de se resolver:
hipotenusa = (cat_oposto**2 + cat_adjacente**2) ** (1/2)

print(f'O comprimento da hipotenusa utilizando módulo é {hipotenusa_modulo:.2f}')
print(f'O comprimento da hipotenusa sem utilizar módulo é {hipotenusa:.2f}')
