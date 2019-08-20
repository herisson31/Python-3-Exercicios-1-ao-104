'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
    mostre uma mensagem com tamanho adaptável.'''

def escreva(msg):
    tam = len(msg) +12
    print('='*tam)
    print(f'      {msg}')
    print('='*tam)


escreva('O universo é a prova que não estamos sozinho, seria um grande desperdicio de espaço')