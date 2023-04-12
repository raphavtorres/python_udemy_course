# Modos:
# r (leitura), w (escrita), x (criação), a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)

# Context Manager --> with (abre e fecha)

path_file = 'C:\\Users\\ct67ca\\Desktop\\pyhtonTorres\\'
path_file += 'file.txt'

# Without "with open()"
# file = open(path_file, 'w')
# file.close()
# With "with open()"
with open(path_file, 'w') as file:
    print('Open file')
    print('And close file')

print(path_file)
