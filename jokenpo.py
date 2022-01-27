#importando biblioteca 'random'
import random
itens = ('Pedra', 'Papel', 'Tesoura')

#o computador pode escolher entre 0, 1 e 2 na mesma sequência dos itens
computador = random.randint(0,2)
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')

#jogador escolhendo um item
jogador = int(input('Qual é a sua jogada?'))

print('''\nJO
KEN
PO!! \n''')

#mostrando qual item o computador escolheu
print('Computador jogou {}\n'.format(itens[computador]))

#possíveis respostas
print('-=' * 10)
if jogador == 0 or jogador == 1 or jogador == 2:
    if jogador == computador:
        print('EMPATE')
    elif jogador == 0 and computador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 0 and computador == 2:
        print('JOGADOR GANHOU')
    elif jogador == 1 and computador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1 and computador == 2:
        print('COMPUTADOR GANHOU')
    elif jogador == 2 and computador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 2 and computador == 1:
        print('JOGADOR GANHOU')
else:
    print('JOGADA INCORRETA') #se jogar um número que não seja 0,1 ou 2
print('-=' * 10)
