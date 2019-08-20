'''072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
   de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove',
          'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete',
          'dezoito','dezenove','vinte')
cont = 0
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <=20:
        break
    '''if num < 0 or num > 20:
        print('Dados Invalidos!')'''

    resp = ' '
    if resp not in 'SN':
        resp = str(input('Valor Inválido, Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            print('fim de execução')
            break
print('O numero que vc digitou foi {}'.format(numero[num]))
print('Fim do programa')