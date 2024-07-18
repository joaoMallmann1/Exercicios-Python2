"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tem peso 1 e a terce
ira tem peso 2. Ao final, mostrar a média do aluno e indicar se ele foi reprovado ou aprovado, a nota de aprovação deve
ser maior ou igual a 6 pontos
"""
notaA = float(input("Digite a nota da primeira prova: "))
notaB = float(input("Digite a nota da segunda prova: "))
notaC = float(input("Digite a nota da terceira prova: "))

pesoA = 1
pesoB = 1
pesoC = 2

media_ponderada = (notaA * pesoA + notaB * pesoB + notaC * pesoC) / (pesoA + pesoB + pesoC)
notaAprovacao = 6

if media_ponderada >= notaAprovacao:
    print("Aprovado")
    print(f"Média ponderada: {media_ponderada:.2f}")
else:
    print("Reprovado")
    print(f"Média ponderada: {media_ponderada:.2f}")

