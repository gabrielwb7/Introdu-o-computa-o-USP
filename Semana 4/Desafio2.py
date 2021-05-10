numero = input('Digite o número por favor:')

inicial = numero[0]
i = numero[1]
adjacente = True

while numero != 0 and not adjacente:
    if inicial != i:
        inicial = numero[0 + 1]
        adjacente = True

