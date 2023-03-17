# Valores padrão para parâmetros em funções Python + NoneType e None

# 0 é um false value
# Por isso eu uso None, pois a pessoa podia passar 0 mas n ia ser printado
# Neste caso eu testo se estou ou não recebendo o "z"

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
