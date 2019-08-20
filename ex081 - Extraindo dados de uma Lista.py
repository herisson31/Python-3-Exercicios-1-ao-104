'''081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

num = list()
cont = 0
while True:
    num.append(int(input('Digite um numero: ')))
    cont += 1

    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        num.append(v)
    elif v % 2 == 1:
        num.append(v)
num.sort(reverse=True)
print('Lista: {}'.format(num))
print(f'Foram digitado {cont} numeros')
if 5 in num:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')
