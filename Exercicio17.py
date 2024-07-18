"""
Faça um programa que calcule e mostre a área de um trapézio.
"""

while True:
    baseMaior = float(input("Digite o valor da base maior: "))
    if baseMaior < 0:
        print("Valor inválido. As bases devem ser maiores que 0.")
    else:
        break

while True:
    baseMenor = float(input("Digite o valor da base menor: "))
    if baseMenor < 0:
        print("Valor inválido. As bases devem ser maiores que 0.")
    else:
        break

altura = float(input("Digite o valor da altura: "))

area = (baseMaior + baseMenor) * altura / 2
print(f'A área deste trapézio é igual a {area:.2f}')
