"""
Usando  switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este núme
ro.
"""
while True:
    numero = int(input("Digite um valor entre 1 a 7 para saber a qual dia da semana o mesmo é correspondente: "))
    if numero < 1 or numero > 7:
        print("Valor inválido")
    else:
        break

diaSemana = ''

if numero == 1:
    diaSemana = "Domingo"
elif numero == 2:
    diaSemana = "Segunda-Feira"
elif numero == 3:
    diaSemana = "Terça-Feira"
elif numero == 4:
    diaSemana = "Quarta-feira"
elif numero == 5:
    diaSemana = "Quinta-Feira"
elif numero == 6:
    diaSemana = "Sexta-Feira"
else:
    diaSemana = "Sábado"

print(f'O número {numero} corresponde a {diaSemana}')
