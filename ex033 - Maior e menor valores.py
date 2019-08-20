import math
'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

#usando if
menor = n1
if n2 < n1 and n2 <n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor numero é {}'.format(menor))

maior = n1
if n2 > n1 and n2 >n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero é {}'.format(maior))

#Usando os metodos max e min
'''numero = n1,n2,n3
print('O maior valor é {}'.format(max(numero)))
print('O menor valor é {}'.format(min(numero)))'''
print('Parabéns, executado com sucesso!!!')
