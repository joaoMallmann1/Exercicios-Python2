"""
Calcule as raízes da equação de 2º grau. A variável 'a' tem que ser diferente de 0. Caso seja igual, imprima a mensagem: "
Não é equação de segundo grau".
Se delta for menor que 0, não existe real. Então imprima a mensagem 'não existe raiz'
Se delta for igual a 0, existe uma raiz real. Imprima a raiz e a mensagem 'raiz unica'
Se delta for maior que 0, imprima as duas raízes reais.
"""
import math

print("Equação 2º grau")
while True:
    a = float(input("Informe o valor de a (Deve ser diferente de 0): "))
    if a == 0:
        print("A variável A deve ser diferente de 0: ")
    else:
        break

b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
delta = (b ** 2 - 4 * a * c)

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes da equação são {x1:.2f} e {x2:.2f}")
elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f"A raiz da equação é {x:.2f}")
else:
    print("A equação não possui raízes reais")

