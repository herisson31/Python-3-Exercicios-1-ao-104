'Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''
C = float(input('Digite uma temperatura em graus Cº: '))
f = C / 5*9 + 32
print('Vc digitou {:.2f} Celsius, convertido para fahrenheit fica {:.2f} Fº'.format(C,f))
