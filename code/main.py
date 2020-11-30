# Importações
from random import randint
from time import sleep

# Funções


def menu():
    while True:
        print('-' * 42)
        print('MENU'.center(42))
        print('-' * 42)
        print('0 - Sair')
        print('1 - Iniciar')
        print('-' * 42)
        while True:
            perguntaMenu = int(input('O que deseja fazer? '))
            if perguntaMenu == 0:
                print('-' * 42)
                print('FINALIZANDO O PROGAMA...'.center(42))
                print('-' * 42)
                sleep(1.5)
                break
            elif perguntaMenu == 1:
                print('-' * 42)
                print('Iniciando...'.center(42))
                print('-' * 42)
                sleep(1.5)
                iniciar()
                break
            print('Opção inválida. Tente novamente!')
        if perguntaMenu == 0:
            break

def iniciar():
    pass


# Palavras

listaPalavras = ['amarelo', 'amiga', 'amor', 'ave', 'avião', 'avó', 'balão', 'bebê']

# Iniciar
menu()