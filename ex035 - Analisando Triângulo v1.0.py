'''Desenvolva um programa que leia o comprimento de três retas
   e diga ao usuário se elas podem ou não formar um triângulo.'''
r1 = int(input('Primeiro Segmento: '))
r2 = int(input('Segundo Segmento: '))
r3 = int(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos informadados podem formar um Triangulo')
else:
    print('Os Segmentos informados não podem formar um Tringulo')
