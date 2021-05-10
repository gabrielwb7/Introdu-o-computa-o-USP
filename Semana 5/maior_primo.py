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

def maior_primo(k):
    while ehPrimo(k) == False:
        k = k - 1
        if ehPrimo(k) == True:
            return k