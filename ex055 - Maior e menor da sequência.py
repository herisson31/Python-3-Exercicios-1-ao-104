'''055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
Maiorpeso = 0
Menorpeso = 0
for pess in range(1,6):
    peso = float(input('Digite o pesso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        Maiorpeso = peso
        Menorpeso = peso
    else:
        if peso > Maiorpeso:
             Maiorpeso = peso
        if peso < Menorpeso:
            Menorpeso = peso
print('O maior peso foi {:.2f} Kg'.format(Maiorpeso))
print('O menor peso foi {:.2f} Kg'.format(Menorpeso))
