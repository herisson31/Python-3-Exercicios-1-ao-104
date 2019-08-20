'''079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
   Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
   digitados, em ordem crescente. '''
num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
         num.append(n)
         print('Valor adicionado com sucesso!!!')
    else:
            print('Duplicado, valor já adicionado')
    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print('='*30)
num.sort()
print(f'Lista: {num}')
print('='*30)
print(' Fim!!!')