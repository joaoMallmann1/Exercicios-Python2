"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
- O número digitado ao quadrado
- A raiz quadrada do número digitado
"""
import math

valor = float(input("Digite um valor: "))

if valor > 0:
    print(f'O número é positivo. {valor} ao quadrado é igual a {valor ** 2} e sua raiz quadrada é igual a '
          f'{math.sqrt(valor)}')
else:
    print('Valor invalido')
