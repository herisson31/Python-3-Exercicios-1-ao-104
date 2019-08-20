'''058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
   Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
   foram necessários para vencer.'''
from random import randint
from time import sleep
computador = randint(1,10)
print('Sou seu computador... Tente adivinhar em um numero entre 0 e 10?')
print('Será que vc consegui adivinhar? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Vc acertou com {} tentativas, parabéns!!!'.format(palpite))
print('')
