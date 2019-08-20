'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
   fim e passo. Seu programa tem que realizar três contagens através da função criada:

   a) de 1 até 10, de 1 em 1
   b) de 10 até 0, de 2 em 2
   c) uma contagem personalizada'''

cont = 0
def contador(i,f,p):
    print(f'A contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM!')

# Programa Principal
contador(1,10,1)
contador(20,0,2)
print('Agora é sua vez, personalize um contador:')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas= int(input('Passo:   '))
contador(ini, fim,pas)