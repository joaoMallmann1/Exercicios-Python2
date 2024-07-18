"""
Escreva um menu de opções. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a op
ção for inválida
"""


def escolha():
    operacao = input("Escolha a opção:\n 1 - Soma de 2 números \n 2 - Diferença entre dois números (maior pelo menor)"
                     "\n 3 - Produto entre 2 números \n 4 - Divisão entre dois números (O denominador não pode ser 0: ")
    return operacao


def solicitar_valores():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    return valor1, valor2


def checagem(operacao, valor2):
    while operacao == "4" and valor2 == 0:
            valor2 = int(input("O segundo valor deve ser diferente de 0: "))
    return valor2


def realizar_operacao(operacao, valor1, valor2):
    maior = max(valor1, valor2)
    menor = min(valor1, valor2)
    if operacao == "1":
        resultado = valor1 + valor2
        print(f'{valor1} + {valor2} = {resultado}')
    elif operacao == "2":
        resultado = maior - menor
        print(f'{valor1} - {valor2} = {resultado}')
    elif operacao == "3":
        resultado = valor1 * valor2
        print(f'{valor1} * {valor2} = {resultado}')
    elif operacao == "4":
        resultado = valor1 / valor2
        print(f'{valor1} / {valor2} = {resultado}')


def main():
    operacao = escolha()
    valor1, valor2 = solicitar_valores()
    valor2 = checagem(operacao, valor2)
    realizar_operacao(operacao, valor1, valor2)


main()





