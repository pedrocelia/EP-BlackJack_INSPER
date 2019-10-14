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
print('')
print('Bem vinda(o), {0}, você está prestes a jogar o melhor blackjack de todos os tempos!!!!!' .format(nome))
print('---------------------------------------------------------')
print('')
print('Esse é o BlackJack FOX, se prepare para a melhor experiencia de todas!\n'
      'O BlackJack FOX é um blackjack de casino, onde temos multiplas features '
      'para você se divertir e ganhar dinheiro ao máximo!')
print('---------------------------------------------------------')
print('')
print('REGRAS (basicas):\n'
      'O jogo é jogado com um (ou mais baralhos de 52 cartas). Para isso as cartas têm a seguinte pontuação:\n'
      '•Cartas com números,valem o valor impresso nelas (cartas de 2 a 10)\n'
      '•Cartas de faces (Valete, Dama, Rei) valem 10 pontos.\n'
      '•O Ás pode valer tanto 1 ou 11 pontos O computador irá fazer o papel do croupier.')


print('---------------------------------------------------------')
print('')
init = input('vamos começar?')
print('Você vai começar com 150 reais')
print('---------------------------------------------------------')
print('')
quant_baralhos = int(input('quantos baralhos você vai querer usar? '))
deck = baralho_quant*quant_baralhos



JOGO = True
resultado = 0

while JOGO:
    aposta = int(input("Quanto deseja apostar? "))
    dinheiro = 150 + resultado
    while dinheiro - aposta < 0:
        print("Aposta invalida")
        aposta = int(input("Digite um novo valor de aposta: "))
        if dinheiro - aposta > 0:
            break
    pontos_jogador = 0
    pontos_crupier = 0
    print("Essa é a sua quantia agora: {0}R$".format(dinheiro)) 
        
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
    print('Isso é quantidade de pontos que você tem: {0}' .format(pontos_jogador))
    
    
    for c in cru_car:
        if c in baralho_valores:
            if c == 'A':
                if pontos_crupier + 11 > 21:
                        pontos_crupier+=baralho_valores[c][0]
                else:
                    pontos_crupier += baralho_valores[c][1]
            else:
                pontos_crupier += baralho_valores[c]

    
    while pontos_jogador < 21:
        if pontos_jogador / 2 == 10:
            opcao = input("Suas opções são: SPLIT, CARTA ou PARAR, escolha: ")
            op = opcao.lower()
            if op == "split":
                mao_1 = cartas[0]
                mao_2 = cartas[1]
        else:
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
    if pontos_jogador<=21:
        if pontos_crupier < pontos_jogador:    
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
    
#PARA MULTIPLAYER    
#não altera o dinheiro                
#    if pontos_jogador > 21 and pontos_crupier > 21:
#        print("Ninguém ganha nada")
#        dinheiro += aposta
     
    # não altera o dinheiro
    if pontos_jogador == 21 and pontos_crupier == 21:
        print("Ninguém ganha nada")
        print('')
        print('ambos fizeram Blackjack')
        resultado = 0
        
    # Dinheiro = 2X o valor apostado     
    elif pontos_jogador < 21 and pontos_crupier > 21:
        print("Parabéns, você ganhou!!")
        print('')
        print('o Crupier estourou com: {0}' .format(pontos_crupier))
        resultado +=  aposta
        
    #Dinheiro = - aposta
    elif pontos_crupier < 21 and pontos_jogador > 21:
        print("Você perdeu")
        print('')
        print('Crupier fez {0} pontos' .format (pontos_crupier))
        resultado -= aposta
        
    # Dinheiro = 2.5X aposta
    elif pontos_jogador == 21 and pontos_crupier != 21:
        print("BLACKJACK!! Parabéns, você ganhou essa rodada!")
        print('')
        print('Crupier estourou com: {}' .format(pontos_crupier))
        resultado += 1.5 * aposta
    
    # Dinheiro = -2.5 x aposta    
    elif pontos_crupier == 21 and pontos_jogador != 21:
        print("BLACKJACK do crupier!!")
        resultado -= 1.5 * aposta
    
    # Dinheiro = 2 x aposta
    elif pontos_jogador > pontos_crupier:
        print("Você ganhou!")
        print('')
        print('Crupier fez {0} pontos' .format(pontos_crupier))
        resultado +=  aposta
    
    # Dinheiro = -2 x aposta    
    else:
        print("Você perdeu")
        print('')
        print('Crupier fez {0} pontos' .format(pontos_crupier))
        resultado -= aposta
    
    
    if dinheiro == 0:
        JOGO = False






















       




