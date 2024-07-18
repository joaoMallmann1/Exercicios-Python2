"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa de
ve calcular o valor a ser pago por aquela refeição.
"""
menu = {
    100: {"Produto": "Cachorro Quente", "Preço": 1.20},
    101: {"Produto": "Bauru Simples", "Preço": 1.30},
    102: {"Produto": "Bauru com Ovo", "Preço": 1.50},
    103: {"Produto": "Hambúrguer", "Preço": 1.20},
    104: {"Produto": "Cheeseburger", "Preço": 1.70},
    105: {"Produto": "Suco", "Preço": 1.40},
    106: {"Produto": "Refrigerante", "Preço": 1.20}
}


def pedir():
    valor_total = 0
    while True:
        codigo = int(input("Digite o código do produto desejado (ou '000' para fechar o pedido): "))
        if codigo == 000:
            break
        elif codigo in menu:
            qtd = int(input("Digite a quantidade a ser comprada do produto: "))
            valor_total += qtd * menu[codigo]["Preço"]
        else:
            print("Código inválido. Insira um dos códigos do cardápio.")
    return valor_total


def main():
    print("Programa de Pedidos em Lanchonete \n \n")
    print("Especificação        Código          Preço\n")
    print("Cachorro Quente      100             1.20\n"
          "Bauru Simples        101             1.30\n"
          "Bauru com Ovo        102             1.50\n"
          "Hambúrguer           103             1.20\n"
          "Cheeseburguer        104             1.70\n"
          "Suco                 105             1.40\n"
          "Refrigerante         106             1.20")
    total = pedir()
    print(f"O total a pagar pelo seu pedido é de ${total:.2f}")


main()
