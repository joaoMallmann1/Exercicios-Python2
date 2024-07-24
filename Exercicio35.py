"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês
Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""
data_str = input("Digite uma data (Separar com traço): ")
dia, mes, ano = map(int, data_str.split('-'))


def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


def validacao(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False

    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if ano_bissexto(ano):
        dias_no_mes[1] = 29

    if dia < 1 or dia > dias_no_mes[mes - 1]:
        return False

    return True


if validacao(dia, mes, ano):
    print(f"A data {data_str} é válida")
else:
    print(f"A data {data_str} não é válida")

