"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se divisível fo
r divisível por 4 e não for divisível por 100.
"""
ano = int(input("Digite o ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("Este é um ano bissexto")
else:
    print("Este não é um ano bissexto")


