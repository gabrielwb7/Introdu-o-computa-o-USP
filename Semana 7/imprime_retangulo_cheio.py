largura = int(input('digite a largura:'))
altura = int(input('digite a altura:'))

while largura >= altura:
    x = altura
    y = largura
    while x != 0:
        print('#' * y, end= '\n')
        x = x - 1
    break