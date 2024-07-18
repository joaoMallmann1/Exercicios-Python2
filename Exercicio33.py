"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo,
e escreva uma mensagem em função do preço novo.
"""
preco_antigo = float(input("Digite o valor do produto a sofrer alteração de precificação: "))

if preco_antigo <= 50:
    preco_novo = preco_antigo + (preco_antigo * 0.05)
    print(f"Produto barato: Reajuste de 5% R${preco_novo:.2f}")
elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo + (preco_antigo * 0.10)
    print(f"Produto normal: Reajuste de 10% R${preco_novo:.2f}")
elif preco_antigo > 100:
    preco_novo = preco_antigo + (preco_antigo * 0.15)
    if 120 < preco_novo <= 200:
        print(f"Produto caro: Reajuste de 15% R${preco_novo:.2f}")
    else:
        print(f"Produto Muito Caro: Reajuste de 15% R${preco_novo:.2f}")


