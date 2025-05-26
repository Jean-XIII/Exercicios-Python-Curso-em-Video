#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = [int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), ]

print(f'O maior número foi {max(lista)} na posição {lista.index(max(lista))+1}')
print(f'O menor número foi {min(lista)} na posição {lista.index(min(lista))+1}')
