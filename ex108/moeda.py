def aumentar(p = 0):
    aumento = p + (p * 13 / 100)
    return aumento

def diminuir(p = 0):
    diminuir = p - (p * 13 / 100)
    return diminuir

def metade(p = 0):
    metade = p / 2
    return metade

def dobro(p = 0):
    dobro = p * 2
    return dobro

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
