"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 a 10, respectivamente,
a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anterior-
mente obedece aos pesos: Trabalho de laboratório: 2; Avaliação semestral: 3; Exame final: 5. De acordo com o resultado,
mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça
todas as verificações necessárias.
"""
while True:
    notaLab = float(input("Digite a nota do trabalho em laboratório: "))
    if notaLab < 0 or notaLab > 10:
        print("Valor inválido")
    else:
        break

while True:
    notaAvaliacao = float(input("Digite a nota da avaliação semestral: "))
    if notaAvaliacao < 0 or notaAvaliacao > 10:
        print("Valor inválido")
    else:
        break

while True:
    notaExame = float(input("Digite a nota do exame: "))
    if notaExame < 0 or notaExame > 10:
        print("Valor inválido")
    else:
        break

peso1 = 2
peso2 = 3
peso3 = 5

mediaP = (notaLab * peso1 + notaAvaliacao * peso2 + notaExame * peso3) / (peso1 + peso2 + peso3)
print("A média ponderada do aluno foi de {0}".format(mediaP))

if 5 > mediaP >= 3:
    print("Aluno em recuperação")
elif mediaP < 3:
    print("Aluno reprovado")
else:
    print("Aluno aprovado")
