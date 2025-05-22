#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metro = float(input('Digite um valor em metros: '))

centimetros = metro * 100
milimetros = metro * 1000

print(f'{metro} metro(s) em centimetros é {centimetros:.1f} cm, e em milimetros é {milimetros:.1f} mm')
