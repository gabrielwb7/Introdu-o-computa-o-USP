numero = int(input('Digite um número inteiro:'))

adjacente = False
ant = numero % 10
numero = numero // 10

while numero > 0 and not adjacente:
    n_atual = numero % 10
    numero = numero // 10
    if n_atual == ant:
        adjacente = True
    ant = n_atual
if adjacente:
    print("sim")
else:
    print('não')