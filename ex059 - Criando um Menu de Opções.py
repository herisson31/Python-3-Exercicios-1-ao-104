'''059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
opção = soma = mult = maior = Novo = 0
n1 = float(input('Digite o Primeiro Numero: '))
n2 = float(input('Digite o Segundo Valor: '))
while opção !=5:
    print('''Suas opções:
    \033[31m[1]\033[m - \033[31mSomar\033[m
    \033[32m[2]\033[m - \033[32mmultiplicar\033[m
    \033[33m[3]\033[m - \033[33mMaior\033[m
    \033[34m[4]\033[m - \033[34mNovos Numeros\033[m
    \033[35m[5]\033[m - \033[35mSair do programa\033[m''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {:.0f} + {:.0f} é \033[34m{:.0f}\033[m'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação de {:.0f} x {:.0f} é \033[34m{:.0f}\033[m'.format(n1,n2,mult))
    elif opção == 3:
        if n1 > n2 and n2 > n1:
            maior = n1
        else:
            maior = n2
            print('O maior valor de {:.0f} e {:.0f} é \033[34m{:.0f}\033[m'.format(n1,n2,maior))
    elif opção == 4:
        print('Digite Novamente novos Valores!')
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção Inválida!')

print('Fim do programa, Volte Sempre!')

