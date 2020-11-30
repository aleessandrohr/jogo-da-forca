# Importações
from random import randint

# Funções


# Palavras

listaPalavras = ['amarelo', 'amiga', 'amor', 'ave', 'avião', 'avó', 'balão', 'bebê']
palavraFormando = ''

# Sorteio 

númeroSorteado = randint(0 , 7)
palavraSelecionada = listaPalavras[númeroSorteado]

# Jogo da Forca

print(f'A palavra selecionada foi {palavraSelecionada} e tem {len(palavraSelecionada)} letras.')
for letra in range (len(palavraSelecionada)):
    print('- ', end='')
print()

letraRepetida = ''
while True:
    letraChutada = str(input('Qual a letra? ')).lower()
    perguntaLetraRepetida = 's'
    if letraChutada in letraRepetida:
        while True:
            perguntaLetraRepetida = str(input(f'A letra {letraChutada} é repetida. \nDeseja mesmo escolher essa letra? [S/N] ')).lower()
            if perguntaLetraRepetida in 'SsNn':
                break
    if perguntaLetraRepetida == 's':
        if letraChutada in palavraSelecionada:
            print('Letra certa.')
            palavraFormando += letraChutada
            if palavraFormando == palavraSelecionada:
                break
        else:
            print('Letra errada.')
    else:
        print('Letra desconsiderada.')  
    letraRepetida += letraChutada