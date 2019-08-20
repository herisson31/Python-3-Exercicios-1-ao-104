''' 080: Crie um programa onde o usuário possa digitar cinco valores
    numéricos e cadastre-os em uma lista, já na posição correta de inserção
    (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

num = []

for i, v in enumerate(0,5):
    num.append(int(input('Digite um valor: ')))
print(f'O valor {v} na posição {i}')