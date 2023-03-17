"""
args --> argumentos não nomeados
* --> *args (empacotamento e desempacotamento)
"""

# revisão desempacotamento
x, y, *resto = 1, 2, 3, 4
print("Guardando o resto em uma lista: ", x, y, resto)

# def soma(x, y):
#   return x+y


def soma(*args):  # args está sendo desempacotado
    total = 0
    for numero in args:
        total += numero
    return total  # uma tupla


print("Soma: ", soma(1, 2, 3, 4, 5, 6))

# Exemplo de desempacotamento em outro contexto
numeros = 1, 2, 3, 4, 5, 6  # isso é uma tupla

print("Print da tupla (empacotado): ", numeros)
print("Print da tupla desempacotada: ", *numeros)  # print desempacotado
