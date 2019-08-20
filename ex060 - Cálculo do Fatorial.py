'''060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
#from math import factorial
from time import sleep
n = int(input('Digite um valor:' ))
#f = factorial(n)
c = n
f = 1
print('CALCULANDO FATORIAL...')
sleep(3)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    sleep(1)
    print(f)
print('\n{} é o fatorial de {} '.format(f, n))

