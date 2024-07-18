"""
Dados 3 valores A, B e C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo e
scaleno, equilátero ou isóscele.
"""
a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))


def verificacao(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        if a == b == c:
            tipo = "Equilátero"
        elif a == b or b == c or c == a:
            tipo = "Escaleno"
        else:
            tipo = "Isósceles"

        return True, tipo
    else:
        return False, None


triangulo, tipo = verificacao(a, b, c)
if triangulo:
    print(f"Os valores indicados formam um triângulo do tipo {tipo}")
else:
    print("Os valores não formam um triângulo válido")



