"""
Escreva um programa que, dada a idade de um nadador, o classifica em uma das seguintes categorias:

CATEGORIA       IDADE
Infantil A      5 a 7
Infantil B      8 a 10
Juvenil A       11 a 13
Juvenil B       14 a 17
Sênior          18>
"""
idade = int(input('Digite sua idade: '))
if idade in [5, 6, 7]:
    print("Infantil A")
elif idade in [8, 9, 10]:
    print("Infantil B")
elif idade in [11, 12, 13]:
    print("Juvenil A")
elif idade in [14, 15, 16, 17]:
    print("Juvenil B")
else:
    print("Sênior")
