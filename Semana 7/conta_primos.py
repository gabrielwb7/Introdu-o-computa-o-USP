def ehPrimo(k):
    cont = 2
    primo = True

    while (cont < k and primo):
        primo = not ((k % cont) == 0)
        cont = cont + 1

    if primo:
        return True
    else:
        return False

def n_primos(k):
    i = 2
    cont = 0
    limitador = k
    while i <= limitador:
        if (ehPrimo(i)):
            cont = cont + 1
        i = i + 1
    return cont

