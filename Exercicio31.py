"""
Faça um programa que receba altura e peso de uma pessoa, de acordo com a tabela, verifique e mostre qual a classificação
dessa pessoa
"""
altura = float(input("Digite a altura da pessoa: "))
peso = float(input("Digite o peso da pessoa: "))

if altura < 1.20 and peso <= 60:
    print("Classificação A")
elif 1.20 <= altura <= 1.70 and peso <= 60:
    print("Classificação B")
elif altura > 1.70 and peso <= 60:
    print("Classificação C")
elif altura < 1.20 and 60 < peso <= 90:
    print("Classificação D")
elif 1.20 <= altura <= 1.70 and 60 < peso <= 90:
    print("Classificação E")
elif altura > 1.70 and peso > 90:
    print("Classificação F")
elif altura < 1.20 and peso > 90:
    print("Classificação G")
elif 1.20 <= altura <= 1.70 and peso > 90:
    print("Classificação H")
else:
    print("Classificação I")

