# Black Jack Mais top do mundo.

import random

baralho_valores = {2:2,
           3:3,
           4:4,
           5:5,
           6:6,
           7:7,
           8:8,
           9:9,
           10:10,
           'J':10,
           'Q':10,
           'K':10,
           'A':[1,11]}

baralho_quant = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']

nome=input('qual é o seu nome? ')

print('---------------------------------------------------------')
print('Bem vinda(o), {0}, você está prestes a jogar o melhor blackjack de todos os tempos!!!!!' .format(nome))
print('---------------------------------------------------------')
print('Esse é o BlackJack FOX, se prepare para a melhor experiencia de todas!\n'
      'O BlackJack FOX é um blackjack de casino, onde temos multiplas features '
      'para você se divertir e ganhar dinheiro ao máximo!')
print('---------------------------------------------------------')
print('REGRAS (basicas):\n'
      'O jogo é jogado com um (ou mais baralhos de 52 cartas). Para isso as cartas têm a seguinte pontuação:\n'
      '•Cartas com números,valem o valor impresso nelas (cartas de 2 a 10)\n'
      '•Cartas de faces (Valete, Dama, Rei) valem 10 pontos.\n'
      '•O Ás pode valer tanto 1 ou 11 pontos O computador irá fazer o papel do croupier.')


print('---------------------------------------------------------')
init = input('vamos começar?')
print('Você vai começar com 150 reais')
print('---------------------------------------------------------')

quant_baralhos = int(input('quantos baralhos você vai querer usar? '))
deck = baralho_quant*quant_baralhos



JOGO = True

aposta = int(input("Quanto deseja apostar?"))
dinheiro = 150 - aposta
pontos_jogador = 0
pontos_crupier = 0









    
cartas = random.sample(deck,2)
deck.remove(cartas[0])
deck.remove(cartas[1])

cru_car = random.sample(deck,2)
deck.remove(cru_car[0])

print('Essa é a carta do crupier {0}' .format(cru_car[0]))

   
print('Essas são suas cartas {0}' .format(cartas))

    
for e in cartas:
    if e in baralho_valores:
        if e == 'A':
            if pontos_jogador + 11 > 21:
                pontos_jogador+=baralho_valores[e[0]]
            else:
                pontos_jogador += baralho_valores[e[1]]
        pontos_jogador += baralho_valores[e]    
print('Isso é quantidade de pontos que você tem: {0}' .format(pontos_jogador))


for c in cru_car:
    if c in baralho_valores:
        if e == 'A':
            if pontos_crupier + 11 > 21:
                    pontos_crupier+=baralho_valores[c[0]]
            else:
                pontos_crupier += baralho_valores[c[1]]
        pontos_crupier += baralho_valores[c]


while pontos_jogador < 21:
    opcao = input('Suas opções são:    PARAR    ou   CARTA, escolha: ')
    if opcao == "CARTA":
        cartas = random.sample(deck,1)
        print("Essa é a sua carta{0}".format(cartas))
        for e in cartas:
            if e in baralho_valores:
                pontos_jogador += baralho_valores[e]
                print("Essa é a sua pontuação agora: ", pontos_jogador)

# não altera o dinheiro                
if pontos_jogador > 21 and pontos_crupier > 21:
    print("Ninguém ganha nada")
    dinheiro += aposta
 
# não altera o dinheiro
elif pontos_jogador == 21 and pontos_crupier == 21:
    print("Ninguém ganha nada")
    dinheiro += aposta
    
# Dinheiro = 2X o valor apostado     
elif pontos_jogador < 21 and pontos_crupier > 21:
    print("Parabéns, você ganhou!!")
    dinheiro += 2 * aposta
    
#Dinheiro = - aposta
elif pontos_crupier < 21 and pontos_jogador > 21:
    print("Você perdeu")
    dinheiro = dinheiro
    
# Dinheiro = 2.5X aposta
elif pontos_jogador == 21 and pontos_crupier != 21:
    print("BLACKJACK!!")
    dinheiro += 2.5 * aposta

# Dinheiro = -2.5 x aposta    
elif pontos_crupier == 21 and pontos_jogador != 21:
    print("BLACKJACK do crupier!!")
    dinheiro -= 1.5 * aposta

# Dinheiro = 2 x aposta
elif pontos_jogador > pontos_crupier:
    print("Você ganhou!")
    dinheiro += 2 * aposta

# Dinheiro = -2 x aposta    
else:
    print("Você perdeu")
    dinheiro = dinheiro
 






















       




