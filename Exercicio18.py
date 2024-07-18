"""
Faça um programa que mostre ao usuário um menu com 4 operações matemáticas. O usuário escolhe uma das opções e o seu pro
grama pede então dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""


def escolha_operacao():
    print("Escolha entre as operações: \n 1 - Adição (+)\n 2 - Subtração (-)\n 3 - Multiplicação (*)\n 4 - Divisão (/)")
    operacao = input()
    return operacao


def realizar_operacao(operacao, num1, num2):
    if operacao == "1":
        return num1 + num2
    elif operacao == "2":
        return num1 - num2
    elif operacao == "3":
        return num1 * num2
    elif operacao == "4":
        if num2 != 0:
            return num1 / num2
        else:
            print("Divisão por zero não permitida")


def main():
    while True:
        operacao = escolha_operacao()
        if operacao not in ["1", "2", "3", "4"]:
            print("Valor inválido")
        else:
            break
    num1 = float(input("Digite o primeiro valor da operação: "))
    num2 = float(input("Digite o segundo valor: "))
    resultado = realizar_operacao(operacao, num1, num2)
    if operacao == "1":
        print(f'{num1} + {num2} = {resultado}')
    elif operacao == "2":
        print(f'{num1} - {num2} = {resultado}')
    elif operacao == "3":
        print(f'{num1} * {num2} = {resultado}')
    elif operacao == "4":
        print(f'{num1} / {num2} = {resultado}')


if __name__ == "__main__":
    main()
