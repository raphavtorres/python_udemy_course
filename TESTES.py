# yield from
def gen1():
    print('gen1 STARTS')
    yield 1
    yield 2
    yield 3
    print('gen1 OVER')


def gen2(gen):
    yield from gen()
    print('gen2 STARTS')
    yield 4
    yield 5
    print('gen2 OVER')


gen = gen2(gen1)
for n in gen:
    print(n)
