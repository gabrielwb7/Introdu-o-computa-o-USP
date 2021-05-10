
def ePrimo(n):
    cont = 2
    primo = True
    while (cont < n and primo):
        primo = not ((n % cont) == 0)
        cont = cont + 1
    return primo


def primo():
    n = int(input("Digite um número inteiro: "))
    while n > 0:
        if ePrimo(n):
            print("Primo")
        else:
            print("Não é primo")
        n = int(input("Digite um número inteiro: "))



