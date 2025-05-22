#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
