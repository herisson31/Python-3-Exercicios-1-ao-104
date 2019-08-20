'''041: A Confederação Nacional de Natação precisa de um programa
   que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
hoje = date.today().year
nasc = int(input('Digite o ano de Nascimento: '))
data = hoje - nasc
if data < 9:
    print('Idade até 9 anos, sua idade é {},  Categoria MIRIN'.format(data))
elif data > 9 and data < 14:
    print('Idade entre 9 e 14 anos, sua idade é {}, Categoria INFANTIL'.format(data))
elif data > 14 and data < 19:
    print('Idade entre 14 e 19 anos, sua idade é {}, Categoria JÚNIOR'.format(data))
elif data > 19 and data < 25:
    print('Idade entre 19 e 25 anos, sua idade é {} Categoria SÊNIOR'.format(data))
elif data > 25:
    print('Idade acima de 25, sua idade é {} Categoria MASTER'.format(data))
