def aumentar(p = 0, formato = False):
    aumento = p + (p * 13 / 100)
    if formato is False:
        return aumento
    else:
        return moeda(aumento)

def diminuir(p = 0, formato = False):
    diminuir = p - (p * 13 / 100)
    if formato is False:
        return diminuir
    else:
        return moeda(diminuir)

def metade(p = 0, formato = False):
    metade = p / 2
    if formato is False:
        return metade
    else:
        return moeda(metade)

def dobro(p = 0, formato = False):
    dobro = p * 2
    if formato is False:
        return dobro
    else:
        return moeda(dobro)

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
