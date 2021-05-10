import math

valor_a = float(input('Por favor digite o valor de "a":'))
valor_b = float(input('Por favor digite o valor de "b":'))
valor_c = float(input('Por favor digite o valor de "c":'))

delta = valor_b ** 2 - 4 * valor_a * valor_c

if delta == 0:
    raiz1 = (- valor_b + math.sqrt(delta)) / (2 * valor_a)
    print('a raiz desta equação é', raiz1)

else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (- valor_b + math.sqrt(delta)) / (2 * valor_a)
        raiz2 = (- valor_b - math.sqrt(delta)) / (2 * valor_a)

        if raiz1 <= raiz2:
            print('as raízes da equação são', raiz1, 'e', raiz2)

        else:
            print('as raízes da equação são', raiz2, 'e', raiz1)