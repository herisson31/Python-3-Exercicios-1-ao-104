'''068: Faça um programa que jogue par ou ímpar com o computador.
   O jogo só será interrompido quando o jogador perder, mostrando
   o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
v = 0
while True:
    jogador = int(input('Joque um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'O jogador jogou {jogador} e o computador jogou {computador} e o total foi {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc Venceu!!!')
            v += 1
        else:
            print('Vc Perdeu!!!')
            break
    elif tipo == 'I':
           if total % 2 == 1:
                print('Vc Venceu!!!')
                v += 1
           else:
                print('Vc Perdeu!!!')
                break
    print('Jogue novamente...')
print(f'Game Over! Vc venceu {v} vezez!!!')

