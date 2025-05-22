#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar os espaços).
#Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')

print(nome.upper())
print(nome.lower())
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')
