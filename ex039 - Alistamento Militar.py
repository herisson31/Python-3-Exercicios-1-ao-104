'''039: Faça um programa que leia o ano de nascimento de um jovem e informe,
   de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
   se é a hora exata de se alistar ou se já passou do tempo do alistamento.
   Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
hoje= date.today().year
calc = hoje - nasc
passou = calc - 18
falta = 18 - calc
if calc <= 17:
    print('Vc ainda vai se ALISTAR, falta {} anos !!!'.format(falta))
elif calc == 18:
    print('Esta na hora de se ALISTAR!!!')
elif calc > 18:
    print('Vc já passou do tempo {} anos de se ALISTAR!!!'.format(passou))

