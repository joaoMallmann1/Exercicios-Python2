# Leia um número do usuário. Se esse número for positivo, calcule a raiz quadrada desse número. Se for negativo, mostre
# uma mensagem dizendo que esse valor é inválido
import math

valor = float(input('Digite um valor: '))

if valor > 0:
    print(f'A raiz quadrada de {valor} é igual a {math.sqrt(valor)}')
elif valor < 0:
    print('Valor inválido')
else:
    print('Valor nulo')

