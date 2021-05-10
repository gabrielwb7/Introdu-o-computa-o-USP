def fatorial(n):
    i = 1
    valor = 1
    while i <= n:
        valor = valor * i
        i = i + 1
    return valor
def numero_bino(n,k):
    return fatorial(n) / fatorial(k) * fatorial(n - k)
