#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor númerico. Ex: n = leaint('Digite um n')

def leiaint(n):
    ok = False
    valor = 0
    while True:
        numero = input(n)
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('Digite um número válido.')
        if ok:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
