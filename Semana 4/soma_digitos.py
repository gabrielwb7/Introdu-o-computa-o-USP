
valor = int(input('Digite um número inteiro:'))

soma = 0

while valor != 0:
    resto = valor % 10
    valor = valor // 10
    soma = soma + resto

print(soma)


