'''075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite o ultimo valor: ')))

print('O valor 9 apareceu {} vezes'.format(num.count(9)))
if 3 in num:
    print('O valor 3 aparece na posição {}'.format(num.index(3) +1))
else:
    print('O valor 3 não foi informado!')
print('Os valores pares são: ', end=' ')
for n in num:
    if n % 2 == 0:
        print('{}'.format(n), end=' ')
