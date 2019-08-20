'''067: Faça um programa que mostre a tabuada de vários números,
   um de cada vez, para cada valor digitado pelo usuário.
   O programa será interrompido quando o número solicitado for negativo. '''
mult = 0

while True:
    num = int(input('Digite um numero: '))
    print('-'*30)
    if num < 0:
        break
    for c in range(1,11):
        mult = num * c
        print(f'{num} x {c} = {mult}')
    print('-'*30)
print('FIM!!!')
