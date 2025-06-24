#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: De 1 até 10, de 1 em 1; De 10 até 0, de 2 em 2; Uma contagem personalizada.

def contador(i, f, p):
    if i < f:
        for c in range(i, f, p):
            print(c, end = ' ')
        print()
    else:
        for c in range(i, f, -p):
            print(c, end = ' ')
        print()
        
contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
