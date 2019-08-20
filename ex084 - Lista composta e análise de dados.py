'''084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
   No final, mostre:
   A) Quantas pessoas foram cadastradas.
   B) Uma listagem com as pessoas mais pesadas.
   C) Uma listagem com as pessoas mais leves.'''

grupo = []
dados = []
mai = men = total = 0
while True:
    dados.append(input('Nome: '))
    dados.append(input('Peso: '))
    if len(grupo) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    grupo.append(dados[:])
    dados.clear()
    total += 1


    resp = ' '
    while resp not in 'NS:':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('Fim!!!')
print(f'Lista de pessoas {grupo}')
print(f'Ao todo vc cadastrou {total} pessoas!')
print(f'O maior peso foi {mai}kg, Peso de', end=', ')
for p in grupo:
    if p[1] == mai:
       print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {men}Kg, Peso de', end=', ')
for p in grupo:
    if p[1] == men:
       print(f'{p[0]}', end=' ')
print()