"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário
imprima "Empréstimo não concedido", caso contrário imprima "Empréstimo concedido"
"""
salario = float(input("Digite o valor do salário do funcionário: "))
emprestimo = float(input("Digite o valor do emprestimo: "))

if emprestimo > salario * 0.20:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")
