'''094: Crie um programa que leia nome, sexo e idade de várias pessoas,
   guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, por favor digite apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()
        if resp in 'SN':
            break
        print('Erro, digite somente S ou N')
    if resp == 'N':
        break

print('='*30)
print(f'A) Foram cadastrada {len(galera)} pessoas')
media = soma / len(galera)
print(f'B) A media da idade é {media:5.2f} ')
print('C) Lista de mulheres cadastradas', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'\n{p["nome"]}, ', end='')
print('\nD) Pessoas com idade acima da media acima!')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k , v in p.items():
            print(f'{k} = {v}, ', end=' ')
        print()
print('<<<ENCERRADO>>>')




