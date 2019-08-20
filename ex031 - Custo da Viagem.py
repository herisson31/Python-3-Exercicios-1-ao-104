'''031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
   Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
   200Km e R$0,45 parta viagens mais longas.'''

viagem = float(input('Qual a distancia da viagem em Km: '))
if viagem < 200:
    valor = viagem *0.50
    print('Sua viagem abaixo 200km')
    print('Vc digitou {:.0f}km ficará em R${:.2f}'.format(viagem,valor))
if viagem > 200:
    valor = viagem * 0.45
    print('Sua viagem acima de 200km')
    print('Vc digitou {:.0f}km ficará em R${:.2f}'.format(viagem,valor))
print('Tenha uma boa viagem!!!')
