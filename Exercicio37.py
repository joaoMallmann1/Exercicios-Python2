"""
As tarifas de certo parque de estacionamento são as seguintes:

- 1º e 2º hora: R$1,00 cada
- 3º e 4º hora: R$1,40 cada
- 5º hora e seguintes: R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pa
gará por duas horas, o mesmo se tivesse ficado 120 minutos. Os momentos de chegada do parque e partida deste são apresen
tados na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará "dez para uma
da tarde". Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e partida, escreva na tela o pre
ço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão num intervalo não superior a 24 horas. Portan
to, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a part
ida ocorreu no dia seguinte ao da chegada.
"""
import math


def ler_horario(mensagem):
    while True:
        try:
            entrada = input(mensagem)
            hora, minuto = map(int, entrada.split())
            if 0 <= hora < 24 and 0 <= minuto < 60:
                return hora, minuto
            else:
                print("Horário inválido. Certifique-se de que as horas estão entre 0 e 23 e os minutos entre 0 e 59.")
        except ValueError:
            print("Entrada inválida. Por favor, digite os valores no formato 'HH MM'.")


def calculo_minutos(hora, minutos):
    return hora * 60 + minutos


def calculo_tempo_estacionamento(hora_chegada, minuto_chegada, hora_partida, minuto_partida):
    minuto_chegada = calculo_minutos(hora_chegada, minuto_chegada)
    minuto_partida = calculo_minutos(hora_partida, minuto_partida)

    if minuto_partida < minuto_chegada:
        minuto_partida += 24 * 60

    return minuto_partida - minuto_chegada


def calculo_preco(horas):
    if horas <= 2:
        return horas * 1.00
    elif horas <= 4:
        return 2 * 1.00 + (horas - 2) * 1.40
    else:
        return 2 * 1.00 + 2 * 1.40 + (horas - 4) * 2.00


hora_chegada, minuto_chegada = ler_horario("Digite a hora e minuto de chegada (HH MM): ")
hora_partida, minuto_partida = ler_horario("Digite a hora e minuto de partida (HH MM): ")

minutos_totais = calculo_tempo_estacionamento(hora_chegada, minuto_chegada, hora_partida, minuto_partida)

horas_a_pagar = math.ceil(minutos_totais / 60)

valor_a_pagar = calculo_preco(horas_a_pagar)

print(f"O valor a pagar pelo estacionamento é de R${horas_a_pagar:.2f} pelo tempo de permanência de {minutos_totais} minutos")