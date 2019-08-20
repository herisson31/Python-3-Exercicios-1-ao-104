'''044: Elabore um programa que calcule o valor a ser pago por um produto,
   considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
opção = 0
preço = float(input('Digite o preço do produto: R$ '))
print('''Formas de pagamento:
[1] - à vista dinheiro/cheque: 10% de desconto
[2] - à vista no cartão: 5% de desconto
[3] - em até 2x no cartão: preço formal
[4] - 3x ou mais no cartão: 20% de juros''')
opção = int(input('Escolha uma forma de pagamento acima: '))
vd = preço - (preço * 10/100)
vc = preço - (preço * 5/100)
tresvezes = preço + ( preço * 20/100)
if opção == 1:
    print('Vc pagou R${:.2f} à vista, ganhou DESCONTO de 10% e ficou R${:.2f}'.format(preço,vd))
elif opção == 2:
    print('Vc pagou R${:.2f} à vista no cartão, ganhou DESCONTO de 5% e ficou R$ {:.2f}'.format(preço,vc))
elif opção == 3:
    print('Vc pagou R${:.2f} em 2x no cartão preço normal R${:.2f} sem juros'.format(preço,preço))
elif opção == 4:
    print('Vc pagou R${:.2f} em 3x ou mais no cartao, com o juro de 20%, ficou R${:.2f}'.format(preço,tresvezes))





