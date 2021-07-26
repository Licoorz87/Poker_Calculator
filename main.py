from handRanking import handRanking, maxCard
from itertools import combinations
from sys import platform
from os import system

def clear():
    platformUsed = platform[0]

    if platformUsed == 'w':
        system('cls')
    
    else:
        system('clear')


def defineLanguage():
    while True:
        print('[1] English')
        print('[2] Português')

        language = input('>> ')
        clear()

        if language[0] in '12':
            break

    if language[0] == '1':
        listOfSentences = ['Number of Players?', '\033[1;31mOnly Numbers!\033[m', 'Cards of Player', '\033[1;31mSome Card is Not Correct\033[m', 
                            'Turn or River?', '\033[1;31mWrite turn Or river!\033[m', 'SCHD']

    else:
        listOfSentences = ['Número de Jogadores?', '\033[1;31mApenas Números!\033[m', 'Cartas do Jogador', 
                            '\033[1;31mAlguma Carta não está Correta!\033[m', 'Turn ou River?', '\033[1;31mEscreva turn Ou river!\033[m', 'CEPO']


    return listOfSentences


def main(listOfSentences):
    # Create Main Deck
    deckOfCards = []

    for suit in listOfSentences[6]:
        for i in range(1, 14):
            deckOfCards.append(f'{i}{suit}')


    # Define Number Of Players
    while True:
        try:
            numberOfPLayers = int(input(f'{listOfSentences[0]}\n>> '))
            clear()

            if numberOfPLayers > 1:
                break

        except:
            clear()
            print(f'{listOfSentences[1]}')


    # Define Players' Deck
    while True:
        deckOfPlayers = list()
        for number in range(numberOfPLayers):
            deck = input(f'{listOfSentences[2]} {number+1} >> ').upper().split()
            deckOfPlayers.append(deck)
            if len(deck) != 2:
                clear()
                print(f'{listOfSentences[3]}')
                okCheck = False
                break
            
            okCheck = True
            for card in deck:
                if card not in deckOfCards:
                    clear()
                    print(f'{listOfSentences[3]}')
                    okCheck = False
                    break

            if okCheck is False:
                break
        
        # Remove Plyers' Cards Of Main Deck
        if okCheck is True:
            for deck in deckOfPlayers:
                for card in deck:
                    deckOfCards.remove(card)

            clear()
            break


    # Define Turn Or River
    while True:
        round = input(f'{listOfSentences[4]}\n>> ').lower()

        if round[0] in 'tr':
            clear()
            break
        
        else:
            clear()
            print(f'{listOfSentences[5]}')


    # Define Cards In Table
    while True:
        if round[0] == 't':
            cardsInTable = input('Flop:\n>> ').upper().split()
            numberOfCards = 3

        else:
            cardsInTable = input('Flop & River:\n>> ').upper().split()
            numberOfCards = 4

        okCheck = True
        for card in cardsInTable:
            if card not in deckOfCards:
                clear()
                print(f'{listOfSentences[3]}')
                okCheck = False
                break

        if len(cardsInTable) != numberOfCards:
            clear()
            print(f'{listOfSentences[3]}')
            okCheck = False

        # Remove Cards In Table Of Main Deck
        if okCheck is True:
            for card in cardsInTable:
                deckOfCards.remove(card)

            clear()
            break

    return deckOfCards, deckOfPlayers, cardsInTable, numberOfCards, numberOfPLayers


def playersProbability(deckOfCards, deckOfPlayers, cardsInTable, numberOfCards, numberOfPlayers):
    # Calculate All Games Possibles
    allGamesPossibles = combinations(deckOfCards, 5 - numberOfCards)
    allGamesPossibles = list(allGamesPossibles)

    # Number of Wins
    wins = list(i for i in range(numberOfPlayers))

    # Simulation All Games
    for gamePossible in allGamesPossibles:
        deckOfPlayersInGamePossible = deckOfPlayers.copy()
        cardsInTableInGamePossible = cardsInTable.copy()

        for number in range(5 - numberOfCards):
            cardsInTableInGamePossible.append(gamePossible[number])
        
        for number in range(numberOfPlayers):
            for numberOfCards in range(5):
                deckOfPlayersInGamePossible[number].append(cardsInTableInGamePossible[numberOfCards])


        # Ranking Of Players' Deck
        bestHandIndex = None
        bestRanking = 0
        bestCardsToTiebreaker = None
        bestKicker = None

        for numberPlayerIndex, playerDeck in enumerate(deckOfPlayersInGamePossible):
            ranking, cardsToTiebreaker, kicker = handRanking(playerDeck)

            if ranking > bestRanking:
                bestHandIndex = numberPlayerIndex
                bestRanking = ranking
                bestCardsToTiebreaker = cardsToTiebreaker
                bestKicker = kicker

            elif ranking == bestRanking:
                if bestCardsToTiebreaker != [False]:
                    bestCardsToTiebreakerTest = bestCardsToTiebreaker.copy()
                    cardsToTiebreakerTest = cardsToTiebreaker.copy()

                    for repeat in range(len(bestCardsToTiebreakerTest)):
                        maxBestCard = max(bestCardsToTiebreakerTest)
                        maxTentativeCard = max(cardsToTiebreakerTest)

                        if maxTentativeCard > maxBestCard:
                            # VAI LA NO OUTRO CODIGO
                            # TEM O OUTRO ERRO TBM


                
                else:
                    pass

            

clear()
listOfSentences = defineLanguage()
while True:
    deckOfCards, deckOfPlayers, cardsInTable, numberOfCards, numberOfPlayers = main(listOfSentences)
    playersProbability(deckOfCards, deckOfPlayers, cardsInTable, numberOfCards, numberOfPlayers)
    clear()



# se colocar 87C funcionara