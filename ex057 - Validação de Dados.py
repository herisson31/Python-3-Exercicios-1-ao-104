'''057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
   Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0:2]
while sexo not in 'MASCULINOmasculino' and sexo not in 'FEMININOfeminino':
    sexo = str(input('Dados inválidos, Informe seu sexo [M/F]: ')).strip().upper()[0:2]
print('Seu sexo é {}, executado com sucesso!'.format(sexo))
