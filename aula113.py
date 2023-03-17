def mult(*args):
    total = 0
    for numero in args:
        total *= numero
    return total


def impar_par(num):
    return "Par" if num % 2 == 0 else "Impar"


resultado = mult(1, 2, 3, 4, 5)
par_impar = impar_par(resultado)

print(resultado)
print(par_impar)
