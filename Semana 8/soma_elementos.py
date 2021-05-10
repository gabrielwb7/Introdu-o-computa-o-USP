def soma_elementos(k):
    soma = 0
    for i in k:
        soma += i
    return soma


lista = []
x = int(input('Digite o número que deseja adicionar a lista:'))
while x >= 0:
    lista.append(x)
    x = int(input('Digite o número que deseja adicionar a lista:'))

print(soma_elementos(lista))