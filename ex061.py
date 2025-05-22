#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while.

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))

decimo = termo + (10 - 1) * razao

cont = termo

while cont <= decimo:
    print(cont)
    cont += razao

