'''Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.'''

nome = str(input('Digite seu nome: ')).strip().split()
print('Seu primeiro nome é {} e seu ultimo nome é {}.'.format(nome[0],nome[-1]))