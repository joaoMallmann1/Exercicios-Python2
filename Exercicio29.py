"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha nú
meros aleatórios entre 1 e 100, e mostre na tela a pergunta: Qual é a soma de a + b, onde a e b são números aleatórios.
Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas
vezes o aluno acertou.
"""
import random


def pergunta(numero_questao):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print(f"{numero_questao}) {a} + {b} = ", end='')
    resultado = int(input())
    return resultado, a, b


def verificacao(resultado, a, b):
    return resultado == a + b


def main():
    print("Teste de Soma")
    respostas_corretas = 0
    perguntas = []

    for i in range(1, 6):
        resultado, a, b = pergunta(i)
        perguntas.append((resultado, a, b))
        if verificacao(resultado, a, b):
            respostas_corretas += 1

    print("\nResultado: ")
    for idx, (resultado, a, b) in enumerate(perguntas, 1):
        correta = a + b
        status = "correto" if resultado == correta else "incorreto"
        if status == "correto":
            print(f"{idx}) {a} + {b} = {resultado} (CORRETA)")
        else:
            print(f"{idx}) {a} + {b} = {resultado} (INCORRETO, resposta certa: {correta})")

    print(f"\nResultado final: {respostas_corretas}/5")


if __name__ == "__main__":
    main()


