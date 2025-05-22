#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

ano_atual = 2025
maior = menor = 0
for c in range(0, 7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'{menor} pessoas são de menor, e {maior} são de maior')
