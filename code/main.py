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
        print('2 - Informações')
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
            elif perguntaMenu == 2:
                print('-' * 42)
                print('Iniciando...'.center(42))
                print('-' * 42)
                sleep(1.5)
                info()
                break
            print('Opção inválida. Tente novamente!')
        if perguntaMenu == 0:
            break

def iniciar():
    palavraSorteada = listaPalavras[randint(0, len(listaPalavras)-1)]
    palavraFixa = []
    for palavra in (palavraSorteada):
        for letra in (palavra):
            palavraFixa.append(letra)
    letraRepetida = ''
    tamPalavraSorteada = len(palavraSorteada)
    erros = 0
    while True:
        letras = ''
        print('-' * 42)
        print('Info'.center(42))
        print('-' * 42)
        print(f'A palavra sorteada tem {len(palavraSorteada)} letras.')
        if erros == 1:
            print(f'Você tem atualmente {erros} erro.')
        else:
            print(f'Voçê tem atualmente {erros} erros.')
        print('Digite /desistir para desistir.')
        print('Digite /letras para ver as letras repetidas.')
        print('-' * 42)
        for letra in range (tamPalavraSorteada):
            letras += '_ '
        img(erros, letras, tamPalavraSorteada)
        while True:
            palpite = str(input('Digite: ')).lower()
            if len(palpite) == 1:
                break
            elif palpite == '/letras':
                print(f'Letras repetidas: {letraRepetida}')
            elif palpite == '/desistir':
                print(f'Você escolheu desistir.')
                print(f'A palavra era: {palavraSorteada}.')
                break
            else:
                print('Digite apenas uma letra!')
        print()
        if palpite == '/desistir':
            break
        perguntaLetraRepetida = 'y'
        if palpite in letraRepetida:
            print(f'Letra {palpite} repetido.')
            while True:
                perguntaLetraRepetida = str(input('Deseja mesmo prosseguir? [Y/N] ')).lower()
                if perguntaLetraRepetida in 'YyNn':
                    break
                print('Digite Y para sim e N para não.')
        if palpite not in letraRepetida:
            letraRepetida += f'{palpite} '
        if perguntaLetraRepetida == 'y':
            if palpite in palavraFixa:
                print(f'Letra {palpite} certa. Parabéns!')
                print()
                tamPalavraSorteada -= 1
                palavraFixa.remove(palpite)
                if len(palavraFixa) == 0:
                    print(f'Parabéns você acertou! Palavra: {palavraSorteada}.')
                    break
            else:
                print(f'Letra {palpite} errada. Ops!')
                erros += 1
        else:
            print('Letra desconsiderada.')
        if erros == 6:
            img(erros, letras)
            break


def info():
    print(f'Em desenvolvimento.')


def img(erros, letras, tam):
    if erros == 0:
        print(f''' 
   _ _ _ _  
 /        
|
|
|
|
|  Letras faltando: {tam} {letras}
|
 \ _ _ _ _

''')
    elif erros == 1:
        print(f''' 
   _ _ _ _  
 /       | 
|
|
|
|
|  Letras faltando: {tam} {letras}
| 
 \ _ _ _ _
''')
    elif erros == 2:
        print(f''' 
   _ _ _ _  
 /       |
|        |
|        |   
|   
|
|  Letras faltando: {tam} {letras}
|
 \ _ _ _ _
''')
    elif erros == 3:
        print(f''' 
   _ _ _ _  
 /       |
|      -/|
|        |   
|   
|
|  Letras faltando: {tam} {letras}
|
 \ _ _ _ _
''')
    elif erros == 4:
        print(f''' 
   _ _ _ _  
 /       |
|      -/|\-
|        |   
|   
|
|  Letras faltando: {tam} {letras}
| 
 \ _ _ _ _
''')
    elif erros == 5:
        print(f''' 
   _ _ _ _  
 /       |
|      -\|/-
|        |   
|         \-  
|
|  Letras faltando:  {tam} {letras}
|
 \ _ _ _ _
''')
    elif erros == 6:
        print(f''' 
   _ _ _ _  
 /       |
|      -\|/-
|        |   
|      -/ \-
|
|  Letras faltando: {tam} {letras}
|
 \ _ _ _ _
''')

# Palavras

listaPalavras = ['amarelo', 'amiga', 'amor', 'ave', 'avião', 'avó', 'balão', 'bebê']

# Iniciar

menu()