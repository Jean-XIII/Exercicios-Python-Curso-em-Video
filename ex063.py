#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

numero = int(input('Digite um número: '))

cont = 0
t1 = 0
t2 = 1
t3 = 0

print(t1)
print(t2)

while cont <= numero - 3:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont += 1
