'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
 Calcule e mostre o comprimento da hipotenusa.'''
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = co**2 + ca**2
hi= math.sqrt(h)
print('O valor da Hipotenusa é {}'.format(hi))
