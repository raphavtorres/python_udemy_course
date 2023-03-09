nomes = ["Maria", "Helena", "Luiz"]

# cria tupla com índice e valor do iterável
#lista_enumerada = list(enumerate(nomes, start=10))

# next devolve primeiro valor (na vdd o próximo valor de um obj iterável)
# print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

#  Aqui meu enumerate se esgotou
# for item in lista_enumerada:
#     print(item)

# Para eu não esgotar meu enumarator eu coloco direto no for sem usar uma variável
for i, item in enumerate(nomes):
    print(item)
