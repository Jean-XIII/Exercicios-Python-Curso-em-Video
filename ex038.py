#Escreva um programa que leia dois números e compare-os, mostrando na tela uma das mensagens: O primeiro valor é maior, o segundo valor é maior, ou não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    print('O primeiro número é maior')
elif numero2 > numero1:
    print('O segundo número é maior')
else:
    print('O dois número são iguais.')
