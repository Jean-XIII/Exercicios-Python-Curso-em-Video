#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end ='')
            if c > 1:
                print(' X', end = ' ')
            else:
                print(' =', end =' ')
    for c in range(num, 0, -1):
        f *= c
    return f

numero = int(input('Digite um número: '))
escolha = input('Você quer ver o cálculo [S/N]? ').upper()
if escolha == 'S':
    print(fatorial(numero, True))
else:
    print(fatorial(numero))
