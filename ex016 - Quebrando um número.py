'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.'''
import math
n =float(input('Digite um numero real: '))
print('Vc digitou {} e seu numero inteiro é {}.'.format(n,math.trunc(n)))
