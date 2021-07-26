def maxCard(possibleKickers):
    if 1 in possibleKickers:
        return 1

    else:
        return max(possibleKickers)


def handRanking(playerDeck):
    # Divide Into Numbers And Symbols
    deckNumber = list()
    deckSymbol = list()

    for card in playerDeck:
        deckNumber.append(int(card[:-1]))
        deckSymbol.append(card[-1])


    # Switch Symbols In Other Languages For Symbols In English
    symbolsInEnglish = ('H', 'S', 'C', 'D')
    symbolsInOtherLanguage = ('C', 'E', 'P', 'O')

    for num in range(7):
        for numTwo, symbolInEnglish in enumerate(symbolsInEnglish):
            if deckSymbol[num] == symbolsInOtherLanguage[numTwo]:
                deckSymbol.append(symbolInEnglish)
                break
    
    for repeat in range(7):
        deckSymbol.pop(0)


    # Define Ranking

    # Royal Flush
    okCheck = True
    for number in (10, 11, 12, 13, 1):
        if number not in deckNumber:
            okCheck = False
            break
    
    if okCheck is True:
        for symbol in 'HSCD':
            score = 0

            for number in (10, 11, 12, 13, 1):
                for num, card in enumerate(deckNumber):
                    if card == number:
                        if deckSymbol[num] == symbol:
                            score += 1

            if score == 5:
                return 10, [False], [False]


    # Straight Flush
    for number in deckNumber:
        score = 0
        listOfCards = [number]

        for repeat in range(1, 5):
            if number + repeat in deckNumber:
                score += 1
                listOfCards.append(number + repeat)
        
            else:
                break

        cardMax = number + repeat

        if score >= 5:
            for symbol in 'HSCD':
                score = 0

                for card in listOfCards:
                    for num, number in enumerate(deckNumber):
                        if number in listOfCards and deckSymbol[num] == symbol:
                            score += 1

                if score == 5:
                    return 9, [cardMax], [False]
            

    # Four Of a Kind
    for number in deckNumber:
        if deckNumber.count(number) == 4:
            deckNumberTest = deckNumber.copy()

            for repeat in range(4):
                deckNumberTest.remove(number)

            return 8, [number], [maxCard(deckNumberTest)]
    

    # Full House
    for number in deckNumber:
        if deckNumber.count(number) >= 3:
            deckNumberTest = deckNumber.copy()

            for repeat in range(3):
                deckNumberTest.remove(number)

            for numberTwo in deckNumberTest:
                if deckNumberTest.count(numberTwo) >= 2:
                    return 7, [number, numberTwo], [False]

    
    # Flush
    for symbol in deckSymbol:
        if deckSymbol.count(symbol) == 5:
            deckNumberTest = deckNumber.copy()

            listOfMax = list()

            for repeat in range(5):
                number = maxCard(deckNumberTest)
                listOfMax.append(number)
                deckNumberTest.remove(number)


            return 6, [False], [listOfMax]

    
    # Straight
    for number in deckNumber:
        score = 0

        for repeat in range(1, 5):
            if number + repeat in deckNumber:
                score += 1
            
            else:
                break

        if score >= 5:
            return 5, [number + repeat], [False]

    
    # Three Of a Kind
    for number in deckNumber:
        if deckNumber.count(number) == 3:
            deckNumberTest = deckNumber.copy()

            for repeat in range(3):
                deckNumberTest.remove(number)

            listOfCards = list()

            for repeat in range(2):
                card = maxCard(deckNumberTest)
                listOfCards.append(card)
                deckNumberTest.remove(card)

            return 4, [number], [listOfCards]


    # Two Pairs
    for number in deckNumber:
        if deckNumber.count(number) >= 2:
            deckNumberTest = deckNumber.copy()

            for repeat in range(2):
                deckNumberTest.remove(number)
            
            for numberTwo in deckNumberTest:
                if deckNumberTest.count(numberTwo) >= 2:

                    for repeat in range(2):
                        deckNumberTest.remove(numberTwo)

                    return 3, [number, numberTwo], [maxCard(deckNumberTest)]


    # Pair
    for number in deckNumber:
        if deckNumber.count(number) >= 2:
            deckNumberTest = deckNumber.copy()

            for repeat in range(2):
                deckNumberTest.remove(number)

            listOfCards = list()

            for repeat in range(3):
                card = maxCard(deckNumberTest)
                listOfCards.append(card)
                deckNumberTest.remove(card)

            return 2, [number], [listOfCards]

    
    # High Card
    cardMax = maxCard(deckNumberTest)
    deckNumberTest = deckNumber.copy()
    deckNumberTest.remove(cardMax)

    listOfCards = list()

    for repeat in range(4):
        card = maxCard(deckNumberTest)
        listOfCards.append(card)
        deckNumberTest.remove(card)

    return 1, [cardMax], [listOfCards]

# As cartas devem ser colocadas no cardsToTiebreaker de forma correta, se não, uma mão
# 88833 perderia para uma mão 222AA, já que puxaria o maior valor.
# Esse erro acontece no Full House e no Two Pairs