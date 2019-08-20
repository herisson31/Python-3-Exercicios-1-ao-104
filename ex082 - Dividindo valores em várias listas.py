'''082: Crie um programa que vai ler vários números e colocar em uma lista.
   Depois disso, crie duas listas extras que vão conter apenas os valores pares
   e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

num = []
pares = []
ímpares = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('Lista: {}'.format(num))
print('Pares: {}'.format(pares))
print('Ímpar: {}'.format(ímpares))
print('Fim!!!')
