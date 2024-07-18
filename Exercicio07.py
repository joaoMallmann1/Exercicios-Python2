# Faça um programa que receba dois números e mostre o maior. Se forem iguais, imprima a mensagem 'numeros iguais'
valorA = float(input('Digite o valor de A: '))
valorB = float(input('Digite o valor de B: '))

if valorA > valorB:
    print("O primeiro valor é maior que o segundo.")
elif valorB > valorA:
    print("O segundo valor é maior que o primeiro.")
else:
    print('Números iguais')
