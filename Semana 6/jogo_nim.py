
def partida():
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    if n % (m + 1) == 0:
        print('Você começa!')
        jogador = 1

    else:
        print('Computador começa!')
        jogador = 0

    while n > 0:
        if jogador == 0:
            n = n - computador_escolhe_jogada(n,m)
            jogador = 1

        else:
            n = n - usuario_escolhe_jogada(n,m)
            jogador = 0

        if n == 0 and jogador == 0:
            print('Fim do jogo! Você ganhou!')
            break
        elif n == 0 and jogador == 1:
            print('Fim do jogo! O computador ganhou!')
            break

        if n < 2:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print('Agora restam {} peças no tabuleiro'.format(n))

def campeonato():
    cont = 1
    while cont <= 3:
        print('****Rodada',cont, '****\n')
        partida()
        cont = cont + 1
    print('**** Final do campeonato! ****')
    print('Placar: Você 0 X',(cont - 1), 'computador')


def computador_escolhe_jogada(n,m):
    i = 0
    if n <= m:
        i = n
    else:
        if n % (m + 1) == 0:
            i = m
        else:
            peca = 0
            while peca % (m + 1) != n % (m + 1):
                peca = peca + 1
                if peca % (m + 1) == n % (m + 1):
                    i = peca

    if i < 2:
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou {} peças.'.format(i))
    return i
def usuario_escolhe_jogada(n,m):
    num = int(input('Quantas peças você vai tirar?'))
    if num > m or num < 1:
        print('Oops! Jogada inválida! Tente de novo.')
    else:
        if num < 2:
            print('Você tirou uma peça.')
        else:
            print('Você tirou {} peças.'.format(num))
    return num

print('Bem vindo ao jogo do NIM! Escolha:')
print('1 - para jogar partida isolada')
print('2 - para jogar campeonato')
modo = int(input())
if modo == 1:
    print('Você escolheu uma partida única!')
    partida()
else:
    if modo == 2:
        print('Você escolheu um campeonato!')
        campeonato()
    else:
        print('Escolha um modo válido')