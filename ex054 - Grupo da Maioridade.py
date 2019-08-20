'''054: Crie um programa que leia o ano de nascimento de sete pessoas.
   No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import datetime
hoje = datetime.today().year
contMaior = 0
contMenor = 0
for c in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = hoje - nasc
    if idade <= 21:
        contMenor += 1
    elif idade > 21:
        contMaior += 1
print('Temos {} pessoas Maiores de Idade!'.format(contMaior))
print('Temos {} pessoas Menores de Idade!'.format(contMenor))



