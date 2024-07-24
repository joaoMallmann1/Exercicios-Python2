"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular, consi
derar a tabela.
"""
while True:
    valor_venda = float(input("Digite o valor da venda para verificação da comissão: "))
    if valor_venda < 0:
        print("Valor inválido")
    else:
        break

if valor_venda >= 100000:
    comissao = 700 + (valor_venda * 0.16)
elif valor_venda >= 80000:
    comissao = 650 + (valor_venda * 0.14)
elif valor_venda >= 60000:
    comissao = 600 + (valor_venda * 0.14)
elif valor_venda >= 40000:
    comissao = 550 + (valor_venda * 0.14)
elif valor_venda >= 20000:
    comissao = 500 + (valor_venda * 0.14)
else:
    comissao = 400 + (valor_venda * 0.14)

print(f"A comissão desta venda é de R${comissao:.2f}")
