"""
Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. Teste a validade d
esta data para saber se é válida. Teste se o dia forncedio é válido: dia > 0, dia <= 28 para o mês de fevereiro(29 se fo
r um ano bissexto), dia <= 30 em abril, junho, setembro e novembro, dia <= 31 nos demais. Teste a validade do mês: mês >
0 e < 13. Teste a validadde do ano: ano <= ano atual (Use uma constante definida com o valor igual a 2008.) Imprimir "Da
ta válida" ou data inválida no final da execução do programa.
"""
data = input("Digite uma data de nascimento (Separar com traço): ")
dia, mes, ano = map(int, data.split('-'))


def checagem_ano():
    if 0 > ano > 2024:
        return False
    else:
        return True


def checagem_mes():
    if 0 > mes > 13:
        return False
    else:
        return True


def checagem_dias():
    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_no_mes[1] = 29

    if dia < 1 or dia > dias_no_mes[mes - 1]:
        return False

    return True


if checagem_ano() and checagem_mes() and checagem_dias():
    print("Data válida")
else:
    print("Data inválida")

