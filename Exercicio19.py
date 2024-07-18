"""
Faça um programa para verificar se determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos
dois
"""
valor = int(input("Digite um valor para checar se ele é divisível por 3 ou 5: "))

if valor % 3 == 0 and valor % 5 == 0:
    print("Valor divisível por ambos. Inválido.")
elif valor % 3 == 0 and valor % 5 != 0:
    print("Valor divisível por 3")
elif valor % 3 != 0 and valor % 5 == 0:
    print("Valor divisível por 5")
else:
    print("O valor não é divisível nem por 3 nem 5")

