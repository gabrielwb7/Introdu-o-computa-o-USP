def maior_elemento(k):
    return max(k)

lista = []
x = int(input('Digite o número que deseja adicionar a lista:'))
while x >= 0:
    lista.append(x)
    x = int(input('Digite o número que deseja adicionar a lista:'))

print(maior_elemento(lista))