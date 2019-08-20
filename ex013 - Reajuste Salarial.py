'''Faça um algoritmo que leia o salario de um funcionário, com 15% de aumento.'''
salario = float(input('Digite o Salario: '))
perc = salario * 15/100
aumento = salario + perc
print('O funcionario tem um salario de R${:.2f}, com o aumento passará a ser R${:.2f} '.format(salario,aumento))