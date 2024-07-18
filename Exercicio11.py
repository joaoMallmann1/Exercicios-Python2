"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
Por exemplo, o número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior que zero, o programa retor
nará a mensagem 'valor inválido'
"""
import sys

numero = input('Digite um valor maior que 0: ')

if not numero.isdigit() or int(numero) <= 0:
    print('Valor inválido. Digitar um número maior que 0')
    sys.exit()
else:
    soma = sum(int(digito) for digito in numero)
    print(f'A soma dos algarismo de {numero} é igual a {soma}')
