'''061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
   mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('Gerador de PA')
print('-='*20)
primeito = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = 0
cont = 0
while cont <= 10:
    print('{}'.format(razao), end=' >> ')
    termo += razao
    cont += 1
    if cont != 0:
print('Pause!!!')