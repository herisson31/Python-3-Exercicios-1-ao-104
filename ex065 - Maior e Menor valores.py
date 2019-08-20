'''065: Crie um programa que leia vários números inteiros pelo teclado.
   No final da execução, mostre a média entre todos os valores e qual foi
   o maior e o menor valores lidos. O programa deve perguntar ao usuário se
   ele quer ou não continuar a digitar valores.'''
maior = menor = soma = quant = media = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant +=1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp =str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print('A media entre os valores somado é {}'.format(media))
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
print('Fim!')

