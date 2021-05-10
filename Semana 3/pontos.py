import math

num_x1 = int(input('Por favor insira o primeiro número: '))
num_y1 = int(input('Por favor insira o segundo número: '))
num_x2 = int(input('Por favor insira o terceiro número: '))
num_y2 = int(input('Por favor insira o quarto número: '))

valorT= (num_x1 - num_x2) ** 2 + (num_y1 - num_y2) ** 2
dist= math.sqrt(valorT)

if dist >= 10:
    print('longe')

else:
    if dist < 10:
        print('perto')