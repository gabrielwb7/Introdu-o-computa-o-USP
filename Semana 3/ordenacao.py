numero_1 = int(input('Insira o primeiro número: '))
numero_2 = int(input('Insira o segundo número: '))
numero_3 = int(input('Insira o terceiro número: '))

delta = numero_1 <= numero_2
alpha = numero_2 <= numero_3

if delta and alpha:
    print('crescente')

else:
    if numero_1 != numero_2:
        print('não está em ordem crescente')