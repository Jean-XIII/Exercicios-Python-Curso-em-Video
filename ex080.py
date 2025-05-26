# Número intermediario tive que ver na resolução

#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for i in range (0, 5):
    numero = int(input('Digite um número: '))
    if i == 0:
        lista.append(numero)
    elif numero > max(lista):
        lista.append(numero)
    elif numero < min(lista):
        lista.insert(0, numero)
    else:
        pos = 0
        while pos <= len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1


print(lista)
