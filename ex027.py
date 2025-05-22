#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ')
separado = nome.split()

print(f'Seu primeiro nome é {separado[0]}')
print(f'Seu último nome é {separado[len(separado)-1]}')
