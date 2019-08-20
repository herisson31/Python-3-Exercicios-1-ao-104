'''076: Crie um programa que tenha uma tupla única com nomes de produtos
   e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
   organizando os dados em forma tabular.'''
produto = ('Lapis',1,'Borracha',2,'Caderno',10,'muchila',90,
           'cola',2.5,'Papel',9.8,'Tesoura',4,'Apontador',1.5)
print('='*40)
print(f'{"Lista de Preços":^40}')
print('='*40)
for pos in range (0, len(produto)):
    if pos % 2 == 0:
        print(f'{produto[pos]:.<30}', end='')
    else:
        print(f'R${produto[pos]:>7.2f}')
print('='*40)