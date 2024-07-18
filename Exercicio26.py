"""
Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em
km/l e escreva uma mensagem de acordo com a tabela abaixo:

CONSUMO   KM/L    MENSAGEM
menor que  8    Venda o carro
entre    8 e 14   Econômico
maior que  12   Super Econômico
"""


def leitura():
    km = float(input("Digite a distância em km do percurso: "))
    litros = float(input("Digite a quantidade de litros consumidos no percurso: "))
    return km, litros


def calculo(km, litros):
    consumo = km/litros
    print(f'O carro faz {consumo:.2f}Km por L')
    return consumo


def checagem(consumo):
    if consumo <= 8:
        print("Venda o carro!")
    elif consumo >= 8 <= 14:
        print("Econômico")
    else:
        print("Super Econômico")


def main():
    km, litros = leitura()
    consumo = calculo(km, litros)
    checagem(consumo)


main()

