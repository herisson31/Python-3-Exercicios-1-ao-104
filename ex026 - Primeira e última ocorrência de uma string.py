'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase que contenha mais uma letra A: ')).strip().upper()
print('A frase contem {} letras "A", o primeiro "A" aparece na posiçao {} e o ultimo "A" aparece na posição {}'.format(frase.count('A'),frase.find('A')+1,frase.rfind('A')+1))