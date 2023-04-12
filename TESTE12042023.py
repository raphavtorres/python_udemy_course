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





path_file = 'C:\\Users\\ct67ca\\Desktop\\pyhtonTorres\\'
path_file += 'file.txt'


with open(path_file, 'w+') as file:
    # WRITING IN FILE
    file.write('Line 1\n')
    file.write('Line 1\n')
    # write multiple lines ==> receives a iterable
    file.writelines(
        ('Line 3\n', 'Line 4\n')
    )

    # READING FILE
    file.seek(0, 0)  # move the cursor up to read the content
    print(file.read())
    print('Reading...')
    file.seek(0, 0)
    print(file.readline())

    # READING MULTIPLE LINES
    print('READ LINES')
    for line in file.readlines():
        print(line.strip())

print('-' * 40)

with open(path_file, 'r') as file:
    print(file.read())
    
    
    
    
    
    
    
    
path_file = 'C:\\Users\\ct67ca\\Desktop\\pyhtonTorres\\'
path_file += 'file.txt'

# MODOS DE ABERTURA DE ARQUIVO E ENCODING COM WITH OPEN
# w --> deletes the file content and write something new
with open(path_file, 'w') as file:
    ...

# a --> adds new content (good to creating log files)
with open(path_file, 'a') as file:
    ...

# Using encoding
with open(path_file, 'w', encoding='utf8') as file:
    file.write('Atenção')
