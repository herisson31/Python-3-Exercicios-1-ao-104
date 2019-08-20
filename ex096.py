'''Faça um programa que tenha uma função chamada área(),
   que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def calc_area():
    print('<<< CONTROLE DE TERRENOS  >>>')
    larg = int(input('Digite a largura (m): '))
    comp = int(input('Digite o cumprimento (m): '))
    total = larg*comp
    print(f'Calculando a largura de {larg}mt x cumprimento {comp}mt dá um total de {total}m²')

calc_area()

print('='*40)
print('posso imprimir essa função quantas vezes quiser utilisando calc_area() ')
print('='*40)
calc_area()