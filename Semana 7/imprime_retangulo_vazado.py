largura = int(input('digite a largura:'))
altura = int(input('digite a altura:'))

if largura != 0 and altura != 0 :
    x = altura
    y = largura
    if x % 2 == 0:
        while x != 0:
            print('#' * y, end= '\n')
            x = x - 1

    else:
        largura_semp = largura - 2
        altura_semp = altura - 2
        print('#' * y, end='\n')
        while altura_semp != 0:
            print('#',(largura_semp - 2) * ' ', '#', end= '\n')
            altura_semp = altura_semp - 1
        print('#' * y, end='\n')

