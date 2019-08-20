'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
   incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    toti = 1
    partidas.clear()
    for c in range(toti, tot + 1):
        partidas.append(int(input(f'Quantos gols nas partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO, digite apenas S ou N')
    if resp == 'N':
        break
print('='*50)
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
print('='*50)
for k, v in enumerate(time):
    print(f'{k:>2}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('='*50)
while True:
    busca = int(input('Ver dados de qual jogador? [ 999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO, não existe jogador com o codigo {busca}')
    else:
        print(f' --- LEVAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i , g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('='*40)
print('<<<Volte Sempre>>>')


