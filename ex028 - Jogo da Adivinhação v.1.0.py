'''028: Escreva um programa que faça o computador "pensar" em um número inteiro
  entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
  pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
computador = randint(0,5)
print('\033[34m Tente adivinhar em um numero que estou pensando entre 0 e 5.\033[m')
vc = int(input('\033[32mDigite um numero: \033[m'))
print('\033[31mPROCESSANDO...\033[m')
sleep(3)
if vc == computador:
    print('\033[34mVc acertou\033[m')
else:
    print('\033[31mVc perdeu, eu pensei no numero {}!\033[m'.format(computador))