# Leia um numero real. Se o número for positivo, imprima sua raiz quadrada. Do contrário, imprima o número ao quadrado
import math

valor = float(input('Digite um valor: '))

if valor > 0:
    print(f'A raiz quadrada de {valor} é {math.sqrt(valor)}')
elif valor < 0:
    print(f'{valor} ao quadrado é igual a {valor ** 2}')
else:
    print('Valor nulo')
