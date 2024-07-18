"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se for positivo, calcular o
logaritmo deste número
"""
import math

num = int(input('Digite um valor para calcular seu logaritmo: '))

if num < 0:
    print('Número inválido')
else:
    log = math.log(num)
    print(f"O logaritmo natural deste valor é {log:.2f}")



