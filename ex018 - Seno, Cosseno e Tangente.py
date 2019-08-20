'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse ângulo.'''
import math
tri = float(input('Digite o valor do triangulo: '))

print('O valor do seno é {:.2f}'.format(math.sin(math.radians(tri))))
print('O valor do cosseno é {:.2f}'.format(math.cos(math.radians(tri))))
print('O valor da tangente é {:.2f}'.format(math.tan(math.radians(tri))))