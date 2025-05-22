#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome do escolhido.

from random import choice

aluno1 = 'Jean'
aluno2 = 'Yuri'
aluno3 = 'Ygor'
aluno4 = 'Jonathan'
lista = [aluno4, aluno1, aluno2, aluno3]
escolhido = choice(lista)

print(f'O aluno escolhido foi o {escolhido}')
