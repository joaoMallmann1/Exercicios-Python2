# Faça um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença entre ambos
valorA = float(input('Digite o valor de A: '))
valorB = float(input('Digite o valor de B: '))

if valorA > valorB:
    print(f'O primeiro valor é maior que o segundo e a diferença entre {valorA} e {valorB} é de {valorA - valorB}')
else:
    print(f'O segundo valor é maior que o primeiro e a diferença entre {valorB} e {valorA} é de {valorB - valorA}')

