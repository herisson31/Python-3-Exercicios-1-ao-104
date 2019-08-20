'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
from datetime import date
ano = int(input('Digite um ano para analisar: digite 0 para o ano atual! '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é Bissesto!!!'.format(ano))
else:
    print('O ano {} não é Bissesto!'.format(ano))
print('Parabéns, programa executado com sucesso!!!')