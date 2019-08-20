'''089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
   No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
   de cada aluno individualmente.'''
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resp in 'N':
        break
print()
print('-='*10)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-='*10)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
print('-='*10)

while True:
    print('-='*10)
    mostrar = int(input('Escolha o id de um aluno pra mostar nota: [999 pra Interromper: '))
    if mostrar == 999:
        print('FINALIZANDO...')
        break
    if mostrar <= len(ficha) -1:
        print(f'Notas de {ficha[mostrar][0]} são {ficha[mostrar][1]}')
print('   <<< VOLTE SEMPRE! >>>   ')
