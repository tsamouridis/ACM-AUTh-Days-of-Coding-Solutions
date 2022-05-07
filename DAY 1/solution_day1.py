def func(*decksToCheck):
    normalDeck = ['A-0', 'A-1', 'A-2', 'A-3', 'K-0', 'K-1', 'K-2', 'K-3', 'Q-0', 'Q-1', 'Q-2', 'Q-3', 'J-0', 'J-1', 'J-2', 'J-3', '10-0', '10-1', '10-2', '10-3', '9-0', '9-1', '9-2', '9-3', '8-0', '8-1', '8-2', '8-3', '7-0', '7-1', '7-2', '7-3', '6-0', '6-1', '6-2', '6-3', '5-0', '5-1', '5-2', '5-3', '4-0', '4-1', '4-2', '4-3', '3-0', '3-1', '3-2', '3-3', '2-0', '2-1', '2-2', '2-3']
            
    dict = {}   #key = card name, value = number of cards in all the decks 
    for testCard in normalDeck:
        num = 0
        for deck in decksToCheck:
            for card in deck:
                if testCard == card:
                    num += 1
        dict[testCard] = num
        
    numberOfFullDecks = dict[min(dict, key=dict.get)]   #finds the minimum value in dict
    
    cardsLeft = []
    for key in dict:
        if dict[key] != numberOfFullDecks:
            for i in range (dict[key] - numberOfFullDecks):
                cardsLeft.append(key)
    
    return numberOfFullDecks, cardsLeft