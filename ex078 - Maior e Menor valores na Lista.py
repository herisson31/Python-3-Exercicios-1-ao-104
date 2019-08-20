'''078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
   No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

num = []
mai = men = 0
for n in range(0,5):
    num.append(int(input('Digite na posição {} um valor: '.format(n))))
    if n == 0:
        mai = men = num[n]
    else:
        if num[n] > mai:
            mai = num[n]
        if num[n] < men:
            men = num[n]
print(f'Lista de valores: {num}')

print('O maior numero é {} nas posições'.format(mai), end=' ')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end=' ')
print('\nO menor numero é {} nas posições'.format(men), end=' ')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end=' ')
#print('O maior valor esta na {}ª e o menor na posição'.format(num.index(max())))