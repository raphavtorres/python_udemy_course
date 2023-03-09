'''
split e join com list e str
split --> divide string
strip --> tira espaços
join --> une uma string
'''

frase = 'Olha só, que coisa interessante'
lista_palavras = frase.split(' ')

lista_frases = []
for i, frase in enumerate(lista_palavras):
    lista_frases.append(lista_palavras[i].strip())

frases_unidas = ' -- '.join(lista_frases)  # posso utilizar qualquer iterável
print(frases_unidas)
