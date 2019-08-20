'''042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''


r1 = int(input('Primeiro Segmento: '))
r2 = int(input('Segundo Segmento: '))
r3 = int(input('Terceiro Segmento: '))
lado = 0
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos Acima podem formar um triangulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO, todos os lados iguais!')
    elif r1 == r2 != r3:
        print('ISÓSCELES, Dois lados iguais, um diferente!')
    elif r1 != r2 != r3:
        print('ESCALENO, todos os lados diferentes!')
else:
    print('Os segmentos Aima não podem formar um Triangulo')
