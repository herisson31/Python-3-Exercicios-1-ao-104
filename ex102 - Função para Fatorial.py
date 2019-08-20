'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
   a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
   o processo de cálculo do fatorial.'''


def factorial(n, show=False):
    '''
    --> Calcula o valor de um Fatorial
    :param n: O Numero a ser calculado
    :param show: (opcional) mostrar o resultado fatorial
    :return: Mostrar o valor de n fatorial
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f'=', end='')
        f *= c
    return f


print(factorial(5,True))
help(factorial)
