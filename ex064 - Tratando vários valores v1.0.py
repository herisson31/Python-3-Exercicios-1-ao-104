'''064: Crie um programa que leia vários números inteiros pelo teclado.
   O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
   No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

cont= soma = total = n = 0
n = int(input('Digite um valor, [999 pra parar:  '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um valor, [999 pra parar:  '))
print('Foi digitado um total de {} numeros'.format(cont))
print('A soma entre esses numeros é {}'.format(soma))