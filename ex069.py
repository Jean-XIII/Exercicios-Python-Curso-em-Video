#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: Quantas pessoas tem mais de 18 anos; Quantos homens foram cadastrados; Quantas mulheres tem menos de 20 anos.

cont18 = homens = mulheres20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    while idade < 0:
        idade = int(input('Digite um número válido: '))

    sexo = input('Digite seu sexo [M/F]: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite apenas M ou F: ').upper()
    
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    escolha = input('Você que continuar [S/N]? ').upper()
    while escolha != 'S' and escolha != 'N':
        escolha = input('Digite apenas S ou N: '). upper()
    if escolha == 'N':
        break

print(f'{cont18} pessoas tem mais de 18 anos, {homens} homens foram cadastrados, {mulheres20} mulheres tem menos de 20 anos')
