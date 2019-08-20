'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
  o carro custa R$60 por dia e R$0,15 por Km rodado.'''
km = float(input('Digite os Km percorrido: '))
dia = int(input('Quantos dias de aluguel: '))
pordia = 60
porkm = 0.15
calckm = km*porkm
calcdia = dia*pordia
calctotal = calcdia+calckm
print('Vc alugou o carro {} dias e vai pagar R${:.2f}'.format(dia,calcdia))
print('Vc percorreu {:.2f}km e vai pagar R${:.2f} de km rodado'.format(km,calckm))
print('Vc vai pagar o total de R${:.2f}'.format(calctotal))