'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
   Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(* núm):
    cont = maior = 0
    print('='*30)
    print('Analisando os valores')
    
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1

    print(f'\nForam passados {cont} valores', end='')
    sleep(0.3)
    print(f'\nO maior valor {maior} ')
    sleep(0.3)



#Programa Principal
maior(1,2,7,6,9,4,5)
maior(1,23,5,4,6,)