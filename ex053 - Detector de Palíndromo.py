'''053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

   Exemplos de palíndromos:
   APOS A SOPA,
   A SACADA DA CASA,
   A TORRE DA DERROTA,
   O LOBO AMA O BOLO,
   ANOTARAM A DATA DA MARATONA.'''
frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
'''inverso = '' ''' #Utiliza no for
inverso = junto[::-1] #Fas a mesma coisa que o for
'''for letra in range(len(junto) -1, -1, -1):''' #Usando o for
'''inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto,inverso))
if junto == inverso:
    print('A frase forma um PALÍNDROMO!')
else:
    print('A frase NÃO FORMA UM PALÍNDROMO!')