"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal
"""
sexo = input('Informe o sexo da pessoa: ')
altura = float(input('Informe a altura da pessoa: '))

if sexo == 'M' or sexo == 'Masculino' or sexo == 'masculino' or sexo == 'Homem' or sexo == 'm':
    print(f'O peso ideal deste homem é igual a {(altura * 72.7) - 58} kg')
elif sexo == 'F' or sexo == 'Feminino' or sexo == 'feminino' or sexo == 'Mulher' or sexo == 'f':
    print(f'O peso ideal desta mulher é igual a {(altura * 62.1) - 44.7} kg')
