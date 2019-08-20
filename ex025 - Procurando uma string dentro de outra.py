'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input('Digite um nome completo: ')).strip()
print('O Nome contem Silva? {}'.format('silva' in nome.lower()))