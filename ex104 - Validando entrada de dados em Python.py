'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do
   Python, só que fazendo a validação para aceitar apenas um valor numérico.
   Ex: n = leiaInt('Digite um n: ')'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro, digite um numero inteiro valido!\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero inteiro: ')
print(f'Vc digitou o numero {n}')