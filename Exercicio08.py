# Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas
import sys

notaA = float(input('Digite a nota A: '))
if notaA < 0 or notaA > 10:
    print('Nota inválida. A nota A deve estar entre 0 e 10.')
    sys.exit(1)
notaB = float(input('Digite a nota B: '))
if notaB < 0 or notaB > 10:
    print('Nota inválida. A nota A deve estar entre 0 e 10.')
    sys.exit(1)
print(f'A média das duas notas é de {(notaA + notaB) / 2:.1f}')

