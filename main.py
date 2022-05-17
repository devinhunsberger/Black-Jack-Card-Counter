import random
import numpy as np


deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']


def main():
    playerHand = []
    dealerHand = []
    curShoe = 1
    count = 0
    burnCard = burn()
    countStyle = cardCountingStyle()
    numDecks = getShoes()
    shoe = createShoe(numDecks)

    while len(shoe) > 0:
        board = []
        while len(playerHand) < 2:
            #Player Dealt
            playerCard = shoe[getCard(shoe)]
            playerHand.append(playerCard)
            board.append(playerCard)
            shoe.remove(playerCard)
            print('Player Dealt -', playerCard[1], 'of', playerCard[0])
            #Dealer Dealt
            dealerCard = shoe[getCard(shoe)]
            board.append(dealerCard)
            shoe.remove(dealerCard)
            if len(playerHand) == 1:
                print('Dealer Dealt -', dealerCard[1], 'of', dealerCard[0])
            else:
                print('Dealer Dealt Face Down (Hole Card)')

    
def getCard(shoe):
    beta = random.randint(0, len(shoe)-1)
    return beta


def getShoes():
    alpha = int(input('How many decks per shoe? '))
    shoe = createShoe(alpha)
    print('You have chosen', alpha, 'per shoe(s).\n')
    return alpha


def burn():
    burnCard = False
    burn = input('Do you want a hidden burn card (Yes, No)? ')
    if burn == 'Yes':
        burnCad = True
        print('You\'ve chosen to have a hidden burn card.')
    else:
        print('You\'ve chosen to not include a hidden burn card.')
    return burnCard


def cardCountingStyle():
    countingSystems = ['Hi-Low', 'Griffin Ultimate', 'Archer', 'Canfield Expert', 'Zen Count', 'Olsen TruCount']
    for i in countingSystems:
        print(i)
    countingStyle = int(input('Which counting system would you like to use (1-' + str(len(countingSystems)) + ')? ')) - 1
    print('You have chosen the', countingSystems[countingStyle], 'counting system.\n')
    return countingStyle


def getScore(hand):
    pass

    
#Hi-Lo card counting system: simplest in terms of mathematics utilizing -1,0,1 as grading, most beginners and medium level counters
#utilize Hi-Lo
def HiLo(count, board):
    subCount = ['2', '3', '4', '5', '6']
    addCount = ['10', 'Jack', 'Queen', 'King', 'Ace']
    neutralCount = ['7', '8', '9']
    subCnt = 1
    addCnt = 1
    for i in board:
        if i in neutralCount:
            pass
        else:
            if i in subCount:
                count -= subCnt
            else:
                count += addCnt
    return count


def createShoe(numDecks):
    fullShoe = []
    i = 0
    while i < numDecks:
        for j in suit:
            for h in deck:
                fullShoe.append([j, h])
        i += 1
    return fullShoe


if __name__ == '__main__':
    main()
