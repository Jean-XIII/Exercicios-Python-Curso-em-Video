#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaint(n):
    while True:
        try:
            num = int(input(n))
        except:
            print('Erro.')
            continue
        else:
            return num

def leiafloat(n):
    while True:
        try:
            num = float(input(n))
        except:
            print('Erro.')
            continue
        else:
            return num

numero = leiaint('Digite um número inteiro: ')
numero2 = leiafloat('Digite um número com fração: ')
print(f'O número inteiro digitado foi {numero} e o fracionario foi {numero2}')
