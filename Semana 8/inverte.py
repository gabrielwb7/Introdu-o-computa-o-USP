lista = []
x = int(input('Digite um número:'))
while x > 0:
    lista.append(x)
    x = int(input('Digite um número:'))

lista_2 = lista[:]
lista_2.reverse()

for i in lista_2:
    print(i, end= '')
    print()