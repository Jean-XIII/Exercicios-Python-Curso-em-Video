#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

condicao = True
sexo = ''
while condicao:
    sexo = input('Digite seu sexo [M/F]: ').upper()
    if sexo == 'M' or sexo == 'F':
        condicao = False

print(f'Seu sexo é {sexo}')
