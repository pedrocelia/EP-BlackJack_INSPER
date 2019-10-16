# Black Jack Mais top do mundo.

import random
import time

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

PLAYERS={}

casino = 1

print('---------------------------------------------------------')
print('')
print('Bem vindas(os), você está prestes a jogar o melhor blackjack de todos os tempos!!!!!')
print('---------------------------------------------------------')
print('')
time.sleep(2)
print('Esse é o BlackJack FOX, se prepare para a melhor experiencia de todas!\n'
      'O BlackJack FOX é um blackjack de casino, onde temos multiplas features '
      'para você se divertir e ganhar dinheiro ao máximo!')
print('---------------------------------------------------------')
print('')
time.sleep(2)
print('REGRAS (basicas):\n'
      'O jogo é jogado com um (ou mais baralhos de 52 cartas). Para isso as cartas têm a seguinte pontuação:\n'
      '•Cartas com números,valem o valor impresso nelas (cartas de 2 a 10)\n'
      '•Cartas de faces (Valete, Dama, Rei) valem 10 pontos.\n'
      '•O Ás pode valer tanto 1 ou 11 pontos O computador irá fazer o papel do croupier.')

print('---------------------------------------------------------')
print('')
time.sleep(2)
init = input('vamos começar?')
print('Cada jogador começa com 150 reais')
print('---------------------------------------------------------')
print('')
print('O casino tem R$1000, vai encara??')

quant_baralhos = int(input('quantos baralhos você vai querer usar? '))
deck = baralho_quant*quant_baralhos

p = int(input('quantos jogadores: '))

for x in range(1,p+1):
    nome = input('qual é o seu nome? ')
    PLAYERS[nome] = [150, 0, 0]

JOGO = True
dinheiro=150


while JOGO:
    for p,v in PLAYERS.items():
        pontos_jogador = 0
        aposta = float(input("{0} quanto deseja apostar? ".format(p)))
        while v[0] - aposta < 0 and aposta < 0:
            print("Aposta invalida")
            aposta = float(input("Digite um novo valor de aposta: "))
            if v[0] - aposta > 0:
                break
        v[2] = aposta
        v[1] = pontos_jogador 
        pontos_crupier = 0
        print("Essa é a sua quantia agora: {0}R$".format(PLAYERS[p][0]))
           
        cartas = random.sample(deck,2)
        deck.remove(cartas[0])
        deck.remove(cartas[1])

        cru_car = random.sample(deck,2)
        deck.remove(cru_car[0])
        deck.remove(cru_car[1])
       
        print('Essa é a carta do crupier {0}' .format(cru_car[0]))
       
        print('Essas são suas cartas {0}' .format(cartas))
       
        for e in cartas:
            if e in baralho_valores:
                if e == 'A':
                    if pontos_jogador + 11 > 21:
                        pontos_jogador += baralho_valores[e][0]
                    else:
                        pontos_jogador += baralho_valores[e][1]
                else:
                    pontos_jogador += baralho_valores[e]
#        pontos_jogador = soma_mao(cartas, baralho_valores)
        print('Isso é quantidade de pontos que você tem: {0}' .format(pontos_jogador))
              
        while pontos_jogador < 21 :
            print('')
            print('se digitar FIM o jogo acaba!')
            opcao = input('Suas opções são:    PARAR    ou   CARTA, escolha: ')
            op = opcao.lower()
            if op == "carta":
                cartas = random.sample(deck,1)
                deck.remove(cartas[0])
                print("Essa é a sua carta{0}".format(cartas))
                for j in cartas:
                    if j in baralho_valores:
                        if j == 'A':
                            if pontos_jogador + 11 > 21:
                                pontos_jogador += baralho_valores[j][0]
                            else:
                                pontos_jogador += baralho_valores[j][1]
                        else:
                            pontos_jogador += baralho_valores[j]
                        print("Essa é a sua pontuação agora: ", pontos_jogador)
            if op == "parar":
                break
            if op == 'fim':
                JOGO = False
                break
        v[1] = pontos_jogador   

    for c in cru_car:
        if c in baralho_valores:
            if c == 'A':
                if pontos_crupier + 11 > 21:
                        pontos_crupier+=baralho_valores[c][0]
                else:
                    pontos_crupier += baralho_valores[c][1]
            else:
                pontos_crupier += baralho_valores[c]
    maior = 0
    for v in PLAYERS:
        if PLAYERS[v][1] > maior:
            maior = PLAYERS[v][1]
    if maior <= 21 and JOGO:
        while pontos_crupier < 17:
            cru_car = random.sample(deck,1)
            deck.remove(cru_car[0])
            for k in cru_car:
                if k in baralho_valores:
                    if k == 'A':
                        if pontos_crupier + 11 > 21:
                            pontos_crupier += baralho_valores[k][0]
                        else:
                            pontos_crupier += baralho_valores[k][1]
                    else:
                        pontos_crupier += baralho_valores[k]                            
                    if pontos_crupier == 21:
                        break
                       
    for s in PLAYERS:
        pontos_jogador = PLAYERS[s][1]
        aposta = PLAYERS[s][2]
        resultado = 0
        if JOGO:
        # não altera o dinheiro
            if pontos_jogador == 21 and pontos_crupier == 21:
                print('')
                print("Ninguém ganha nada")
                print('')
                print('ambos fizeram Blackjack')
                resultado = 0
               
               
            # Dinheiro = 2X o valor apostado    
            elif pontos_jogador < 21 and pontos_crupier > 21:
                print('')
                print("Parabéns, {0} ganhou!!" .format(s))
                print('')
                print('o Crupier estourou com: {0}' .format(pontos_crupier))
                resultado +=  aposta
               
            #Dinheiro = - aposta
            elif pontos_crupier < 21 and pontos_jogador > 21:
                print('')
                print("{0} perdeu" .format(s))
                print('')
                print('Crupier fez {0} pontos' .format (pontos_crupier))
                resultado -= aposta
               
            # Dinheiro = 2.5X aposta
            elif pontos_jogador == 21 and pontos_crupier != 21:
                print('')
                print("BLACKJACK!! Parabéns, {0} ganhou essa rodada!" .format(s))
                print('')
                print('Crupier estourou com: {0}' .format(pontos_crupier))
                resultado += 1.5 * aposta
           
            # Dinheiro = -2.5 x aposta    
            elif pontos_crupier == 21 and pontos_jogador != 21:
                print('')
                print("BLACKJACK do crupier!!")
                resultado -= 1.5 * aposta
           
            # Dinheiro = 2 x aposta
            elif pontos_jogador > pontos_crupier:
                print('')
                print("{0} ganhou!" .format(0))
                print('')
                print('Crupier fez {0} pontos' .format(pontos_crupier))
                resultado +=  aposta
           #em caso de empate entre os pontos.
            elif pontos_jogador == pontos_crupier:
                print('')
                print('Empate')
                resultado = 0
            
            # Dinheiro = -2 x aposta    
            else:
                print('')
                print("{0} perdeu" .format(s))
                print('')
                print('Crupier fez {0} pontos' .format(pontos_crupier))
                resultado -= aposta
            casino -= resultado
            PLAYERS[s][0] = PLAYERS[s][0] + resultado
            print('essa é a quantidade de agora: {0}' .format(PLAYERS[s][0]))
   
    if PLAYERS[v][0] <= 0:
        JOGO = False 
    
    if casino <= 0:
        print('parabéns voces quebraram o casino')
        JOGO = False
        
print('Obrigado por jogar \n'
      'Volte(em) sempre!')
