"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg):
    return msg


def executa(funcao, texto):
    return funcao(texto)


# saudacao_1 = saudacao
# v = saudacao_1('Bom dia')
# print(v)

v = executa(saudacao, 'Bom dia')
print(v)
