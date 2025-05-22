#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando laço for.

numero = int(input('Digite um número: '))

for cont in range(0, 11):
    soma = numero + cont
    print(f'{numero} + {cont} = {soma}')
