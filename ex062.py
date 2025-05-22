#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))

decimo = termo + (10 - 1) * razao
resp = 1
cont = termo
condicao = True

while cont <= decimo:
    print(cont)
    if cont == decimo:
        resp = int(input('Mais quantos termos você quer mostrar? '))
        decimo += resp * razao
    cont += razao
