"""
Faça um programa que receba três números e os mostre em ordem crescente
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(f"Números em ordem crescente: {a}, {b}, {c}")
