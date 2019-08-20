'''052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num +1):
    if num % c == 0: #Identifica numeros primos
        tot += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} é divisivel {} vezes'.format(num,tot))
if tot == 2: # Confirma o numero primo
    print('\033[34mO numero {} é PRIMO!\033[m'.format(num))
else:
    print('\033[32mO numero {} NÃO É PRIMO!'.format(num))