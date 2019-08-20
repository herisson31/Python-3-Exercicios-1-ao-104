'''045: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
itens = ('PAPEL','TESOURA','PEDRA')
computador = randint(0,2)
print('''Opções para Jogar:
[0] - PAPEL
[1] - TESOURA
[2] - PEDRA''')
jogador = int(input('Faça sua escolha: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-='*10)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-='*10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU!')
    else:
        print('Jogada Invalida!')

elif computador ==1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')

    else:
        print('Jogada Invalida!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Invalida!')
