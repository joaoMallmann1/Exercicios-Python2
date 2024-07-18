"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com
um valor numérico digitado pelo usuário:

(a) Geométrica
(b) Ponderada
(c) Harmônica
(d) Aritmética
"""
import math

print("Cálculo de tipos de médias")

x = float(input("Digite o valor da variável A: "))
y = float(input("Digite o valor da variável B: "))
z = float(input("Digite o valor da variável C: "))

print("Escolha entre os tipos de cálculos: ")
print("A - Média Geométrica")
print("B - Média Ponderada")
print("C - Média Harmônica")
print("D - Média Aritmética \n")

while True:
    media = input()
    if media not in ["A", "B", "C", "D", "a", "b", "c", "d"]:
        print("Valor inválido. Escolha entre as opções disponíveis")
    else:
        break

if media == "A" or media == "a":
    resultado = (x * y * z) ** (1/3)
    print(f"Média Geométrica: ³√{x} * {y} * {z} = {resultado:.2f}")
elif media == "B" or media == "b":
    resultado = (x + 2 * y + 3 * z) / 6
    print(f"Média Ponderada: {x} + 2 * {y} + 3 * {z} / 6 = {resultado:.2f}")
elif media == "C" or media == "c":
    resultado = 3 / (1/x + 1/y + 1/z)
    print(f"Média Harmônica: 3 / (1/{x} + 1/{y} + 1/{z}) = {resultado:.2f}")
elif media == "D" or media == "d":
    resultado = (x + y + z) / 3
    print(f"Média Aritmética: ({x} + {y} + {z}) / 3 = {resultado:.2f}")



