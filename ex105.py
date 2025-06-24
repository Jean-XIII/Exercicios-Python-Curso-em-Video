#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas; A maior nota; A menor notas; A média da turma; A situação(opcional)

def notas(*n, sit = False):
    dicionario = dict()
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n) / len(n)
    if sit == True:
        if dicionario['media'] < 5:
            dicionario['situacao'] = 'Ruim'
        elif 5 <= dicionario['media'] < 7:
            dicionario['situacao'] = 'Razoável'
        else:
            dicionario['situacao'] = 'Bom'

    return dicionario

resp = notas(5.5, 2.5, 1.5, sit = True)
print(resp)
