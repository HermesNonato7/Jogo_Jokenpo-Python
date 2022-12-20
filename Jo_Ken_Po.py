from random import randint
from time import sleep

items = ('PEDRA', 'PAPEL','TESOURA')
computador = randint(0, 2)
print('-=='*18)
jogador = int(input('Por favor, escolha: [0] PEDRA [1] PAPEL  [2] TESOURA: '))

print('-=='*18)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-=='*18)

print(f'O Jogador escolheu: {items[jogador]}.')
print(f'O Computador escolheu: {items[computador]}.')
print('-=='*18)

if jogador == 0:
    if computador == 0:
        print('Empate!')

    elif computador == 1:
        print('Computador venceu!')

    elif computador == 2:
        print('Jogador venceu!!')

    else:
        print('Jogada inválida!')

elif jogador == 1:
    if computador == 0:
        print('Jogador venceu!')

    elif computador == 1:
        print('Empate!')

    elif computador == 2:
        print('Computador venceu!')
    else:
        print('Jagada inválida!')

elif jogador == 2:
    if computador == 0:
        print('Computador venceu!')
        
    elif computador == 1:
        print('Jogador venceu!')

    elif computador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
