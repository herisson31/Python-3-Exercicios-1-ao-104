'''037: Escreva um programa em Python que leia um número inteiro qualquer e
   peça para o usuário escolher qual será a base de conversão:
   1 para binário,
   2 para octal e 3 para hexadecimal.'''
n = int(input('Digite um numero:'))
print('''Escolha uma das opções abaixo:
[1] converter pra BINARIO
[2] converter pra OCTAL
[3] converter pra HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O numero escolhido em BINARIO fica {}'.format(bin(n)[2:]))
elif opção == 2:
    print('O numero escolhido em OCTAL fica {}'.format(oct(n)[2:]))
elif opção == 3:
    print('O numero escolhido em HEXADECIMAL fica {}'.format(hex(n)[2:]))
else:
    print('Opção Invalida!')