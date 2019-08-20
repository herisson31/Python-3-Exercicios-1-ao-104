'''070: Crie um programa que leia o nome e o preço de vários produtos.
   O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
totgasto = contmil = menor = cont = 0
barato = ''
while True:
    print('='*30)
    print('{:=^30}'.format('LOJA BARATÃO'))
    print('='*30)
    produto = str(input('Produto: ')).strip().upper()
    preço = float(input('Preço R$: '))
    cont += 1
    totgasto += preço
    if preço > 1000:
        contmil += 1

#Pode ser assim simplificado
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
        
# ou composta
    '''if preço < menor:
        menor = preço
        barato = produto'''
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if perg == 'N':
        break
print(f'Total da compra R${totgasto:.2f}')
print(f'{contmil} produtos custa mais de R$1.000,00')
print(f'O produto mais barato é {barato} e o valor é R${menor:.2f}')
print('{:=^30}'.format('COMPRA FINALIZADA!!!'))
print('='*30)
