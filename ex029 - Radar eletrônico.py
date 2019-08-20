''' 029: Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
    ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite '''

velocidade = float(input('Digite a Velocidade em Km: '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Vc ultrapassou o limite permitido que é de 80km/h')
    print('Vc deverá pagar uma multa de R${:.2f}'.format(multa))
print('Boa viagem, dirija com segurança!!!')