#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs: Use cores.

def sistema(f):
    ajuda = help(f)
    return ajuda

while True:
    funcao = input('Digite o nome da função que você quer saber o que faz: ').lower()
    
    if funcao == 'fim':
        break
    else:
        sistema(funcao)