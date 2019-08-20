'''036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
        Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
        A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario do comprador: '))
anos = int(input('Digite em quantos anos vai pagar: '))
prestação = casa / (anos * 12)
minimo = salario * 30/100
desconto = salario - prestação
print('\nComprando uma casa no valor de R${:.0f} em {} anos'.format(casa,anos))
print('O valor da prestação será de R${:.0f}'.format(prestação))
if prestação <= minimo:
    print('O emprestimo foi CONCEDIDO!')
else:
    print('O emprestimo foi NEGADO!')
    print('\033[31mPagando essa prestaçao restará apenas R${:.0f} do seu salario, acima dos 30%!\033[m'.format(desconto))

