#Faça um programa que tenha uma lista chamada números[] e duas funções chamadas sorteio() e soma_par(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = list()

def sorteio():
    for c in range(0, 5):
        sorteio = randint(0, 13)
        numeros.append(sorteio)
    print(f'Números sorteados: {numeros}')

def soma_par():
    soma = 0
    for num in numeros:
        if num % 2 ==0:
            soma += num
    print(f'Soma dos números pares: {soma}')
sorteio()
soma_par()
