''' 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
    sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
print()
print(' <<  JOGO DE DADO  >>')
dado = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}

ranking = list()
for k , v in dado.items():
    print(f' - {k} jogou: {v}')
    sleep(1)
print()
print(' <<<    RANKING    >>>')
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i , v in enumerate(ranking):
    print(f'{i +1}ª lugar: {v[0]} com {v[1]}')
    sleep(1)
