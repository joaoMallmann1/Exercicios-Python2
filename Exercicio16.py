"""
Usando switch, escreva um programa que leia um número inteiro entre 1 e 12 e imprima o mês correspondente a este número
"""


def obter_mes(n):
    mes = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

    if n in mes:
        return mes[n]
    else:
        return "Número inválido"


while True:
    try:
        numero = int(input("Insira o valor de 1 a 12 para saber o mês correspondente: "))
        if numero < 1 or numero > 12:
            print("Número fora do intervalo permitido. Tente novamente.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número válido.")

mesAno = obter_mes(numero)
print(f"O número {numero} corresponde ao mês de {mesAno}")
