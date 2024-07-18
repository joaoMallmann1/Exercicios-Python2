"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições de aposentad
oria são: ter trabalhado pelo menos 30 anos; ter pelo menos 65 anos; Ou ter pelo menos 60 anos e ter trabalhado ao menos
25.
"""
idade = int(input('Digite a idade do trabalhador: '))
tempo = int(input('Digite o seu tempo de serviço: '))

if idade >= 60 and tempo >= 25:
    print('O trabalhador pode se aposentar')
elif idade >= 65:
    print('O trabalhador pode se aposentar')
elif tempo >= 30:
    print('O trabalhador pode se aposentar')
else:
    print('O trabalhador não pode se aposentar')
