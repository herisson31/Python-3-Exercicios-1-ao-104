'''062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
   O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('Gerador de PA')
print('-='*20)
primeito = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeito
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' >> ')
        termo += razao
        cont += 1
    print('Pause!!!')
    mais = int(input('Quantos termos vc quer mostrar? '))
print('Progressao finaliza com total de {} termos'.format(total))