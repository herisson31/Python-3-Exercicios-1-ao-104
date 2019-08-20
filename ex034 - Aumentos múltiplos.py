'''034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
   Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
   o aumento é de 15%.'''
salario = float(input('Digite o seu salario: '))
if salario < 1250:
    novo = salario + (salario * 15/100)
    print('Seu salario de R${:.2f}, com o aumento passará a ser R${:.2f}'.format(salario,novo))
if salario > 1250:
    novo = salario + (salario * 10/100)
    print('Seu salario de R${:.2f}, com o aumento passará a ser R${:.2f}'.format(salario,novo))
print('Programa executado com sucesso!!!')