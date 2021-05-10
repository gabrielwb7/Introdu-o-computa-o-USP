def remove_repetidos (k):
    lista_2 =[]
    for i in k:
        if not i in lista_2:
            lista_2.append(i)
    return (sorted(lista_2))

lista = []
x = int(input('Digite o número que deseja adicionar a lista:'))
while x >= 0:
    lista.append(x)
    x = int(input('Digite o número que deseja adicionar a lista:'))

print(remove_repetidos(lista))
