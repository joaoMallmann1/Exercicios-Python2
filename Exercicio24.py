"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre
o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado de destino do p
roduto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado
digitado não for válido, mostrar uma mensagem de erro.
"""
valor = float(input("Digite o valor do produto: "))

while True:
    estado = input("Digite o estado de destino do produto (MG; SP; RJ; MS): ")
    if estado not in ['MG', 'SP', 'RJ', 'MS']:
        print('Estado inválido. Digite novamente: ')
    else:
        break

if estado == 'MG':
    imposto = valor * 0.07
    valorF = valor + imposto
    print(f'O valor final para Minas Gerais com os impostos é de R${valorF:.2f}')
elif estado == 'SP':
    imposto = valor * 0.12
    valorF = valor + imposto
    print(f'O valor final para São Paulo com os impostos é de R${valorF:.2f}')
elif estado == 'RJ':
    imposto = valor * 0.15
    valorF = valor + imposto
    print(f'O valor final para o Rio de Janeiro com os impostos é de R${valorF:.2f}')
elif estado == 'MS':
    imposto = valor * 0.08
    valorF = valor + imposto
    print(f'O valor final para Mato Grosso do Sul com os impostos é de R${valorF:.2f}')


