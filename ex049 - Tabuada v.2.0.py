'''049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
   só que agora utilizando um laço for.'''

n = int(input('Digite um valor: '))
print('=-'*10)
for c in range(1,10 + 1):
    mult = n * c
    print('{} x {:2} = {}'.format(n,c, mult))
print('-='*10)

