"""
    746.824.890-70 (746824890)
"""


def formatCPF(cpf):
    cpf_separado = cpf.split('-')
    list_cpf_nove_dig = cpf_separado[0]
    dig_finais_cpf = cpf_separado[1]
    cpf_nove_dig_clean = list_cpf_nove_dig.replace(".", "")  # devolve string
    return cpf_nove_dig_clean, dig_finais_cpf


def calcDigCPF(cpf_nove_dig):
    """
    Calcula os dois últimos digitos do CPF, com base nos nove primeiros
    :return:
    """
    contador_reg = len(cpf_nove_dig) + 1
    list_mult_val = []
    for num in cpf_nove_dig:
        list_mult_val.append(int(num) * contador_reg)
        contador_reg -= 1

    soma_val_cpf = 0
    for num in list_mult_val:
        soma_val_cpf += num

    #  multiplicar soma por 10
    #  obter resto da divisão do resultado anterior por 11
    #  se resto maior 9 = 0, se nao = proprio resto
    operacoes = ((soma_val_cpf * 10) % 11)
    resultado_operacoes = 0 if operacoes > 9 else operacoes
    return resultado_operacoes


def calcPrimDig(cpf_nove_dig):
    return calcDigCPF(cpf_nove_dig)


def calcSegDig(cpf_nove_dig):
    cpf_dez_dig = str(cpf_nove_dig) + str(calcPrimDig(cpf_nove_dig))
    return calcDigCPF(cpf_dez_dig)


def validarCPF(cpf):
    cpf_nove_dig, cpf_dig_finais = formatCPF(cpf)
    calcDigCPF(cpf_nove_dig)
    prim_dig = calcPrimDig(cpf_nove_dig)
    seg_dig = calcSegDig(cpf_nove_dig)
    dig_finais_calc = str(prim_dig) + str(seg_dig)

    if cpf_dig_finais == dig_finais_calc:
        print("CPF VÁLIDO!😎")
    else:
        print("CPF INVÁLIDO!😒")

try:
    cpf = input("Digite seu CPF no formato (___.___.___-__): ")
    if (not '-' in cpf) \
            or (not '.' in cpf) \
            or len(cpf) > 14:
        raise ValueError
    else:
        validarCPF(cpf)
except ValueError:
    print("Digite apenas números, e utilize o formato (___.___.___-__)")
    quit()
