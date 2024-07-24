"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo, ocorre uma redu
ção de conceito quando o aluno tem mais de 20 faltas.
"""
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. O número deve ser de 0 a 10.")
    else:
        break

while True:
    faltas = int(input("Digite o número de faltas do aluno: "))
    if faltas < 0:
        print("Quantidade de faltas inválida.")
    else:
        break

if faltas > 20:
    if nota >= 9:
        conceito = 'B'
    elif nota >= 7.5:
        conceito = 'C'
    elif nota >= 5:
        conceito = 'D'
    elif nota >= 4:
        conceito = 'E'
    else:
        conceito = 'E'
else:
    if nota >= 9:
        conceito = 'A'
    elif nota >= 7.5:
        conceito = 'B'
    elif nota >= 5:
        conceito = 'C'
    elif nota >= 4:
        conceito = 'D'
    else:
        conceito = 'E'

print(f"Com {faltas} e uma média de {nota}, o conceito deste estudante é de {conceito}")
