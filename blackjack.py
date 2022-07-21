from random import shuffle


class Card:
    suit = 0
    number = 0


def createcards():
    cards = 52
    length = 13
    suits = 4
    inc = 0
    stack = [Card() for x in range(cards)]
    for x in range(suits):
        for y in range(length):
            stack[inc].suit = x
            stack[inc].number = y
            inc += 1
    shuffle(stack)
    return stack


def printhand(cardhand):
    value = 0
    for x in range(len(cardhand)):
        if cardhand[x].number < 10:
            print(cardhand[x].number + 1, end=" ")
            value += cardhand[x].number + 1
        elif cardhand[x].number == 10:
            print("Jack", end=" ")
            value += 10
        elif cardhand[x].number == 11:
            print("Queen", end=" ")
            value += 10
        elif cardhand[x].number == 12:
            print("King", end=" ")
            value += 10
        print("of", end=" ")
        if cardhand[x].suit == 0:
            print("Clubs", end="")
        elif cardhand[x].suit == 1:
            print("Spades", end="")
        elif cardhand[x].suit == 2:
            print("Hearts", end="")
        elif cardhand[x].suit == 3:
            print("Diamonds", end="")
        if x < len(cardhand) - 1:
            print(",", end=" ")
    print("\nValue: ", value)
    return value


def playhand(cardhand, stack, handbet, value, handnum):
    ended = False
    askedsplit = False
    inc = 0
    while not ended:
        if cardhand[0].number == cardhand[1].number and not askedsplit:
            print("Hit, Stand, Split, or Double?")
        else:
            print("Hit, Stand, or Double?")
        choice = input()
        if choice == "Hit" or choice == "hit" or choice == "H" or choice == "h" or choice == "Double" or choice == "double" or choice == "D" or choice == "d":
            cardhand.append(stack.pop())
            value[handnum] = printhand(cardhand)
            if value[handnum] > 21:
                print("You have busted")
                ended = True
            elif value[handnum] == 21:
                print("Blackjack")
                ended = True
            if choice == "Double" or choice == "double" or choice == "D" or choice == "d":
                handbet[handnum] *= 2
        elif choice == "Stand" or choice == "stand" or choice == "S" or choice == "s":
            ended = True
        elif (choice == "Split" or choice == "split") and cardhand[0].number == cardhand[1].number:
            splithand = [cardhand.pop(), stack.pop()]
            print("Hand 1:")
            printhand(splithand)
            handbet.append(handbet[handnum])
            value.append(0)
            inc = playhand(splithand, stack, handbet, value, handnum + 1)
            cardhand.append(stack.pop())
            print("Hand 2:")
            printhand(cardhand)
        else:
            print("Please choose hit, stand, or double")
        askedsplit = True
    if inc > handnum:
        return inc
    return handnum


def calcvalue(dealerhand):
    value = 0
    for x in range(len(dealerhand)):
        if dealerhand[x].number < 10:
            value += dealerhand[x].number + 1
        elif dealerhand[x].number >= 10:
            value += 10
    return value


def playdealer(dealerhand, stack):
    print("\nDealer:", end="")
    ended = False
    while not ended:
        dealerhand.append(stack.pop())
        value = calcvalue(dealerhand)
        if value >= 17:
            ended = True


# Main function
loop = True
tokens = 1000
while loop:
    print("Tokens: ", tokens, "\nHow much will you bet?")
    bet = [int(input())]
    if tokens <= 0:
        print("Can't bet")
        bet[0] = 0
    elif bet[0] >= tokens:
        print("Betting all in")
        bet[0] = tokens
    elif bet[0] < 0:
        print("Betting 0")
        bet[0] = 0
    cardstack = createcards()
    hand = [cardstack.pop() for x in range(2)]
    dealer = [cardstack.pop()]
    print("Dealer:")
    printhand(dealer)
    print("")
    print("Current Hand:")
    printhand(hand)
    # Plays hand
    handvalue = [0]
    hands = 0
    hands = playhand(hand, cardstack, bet, handvalue, hands)
    playdealer(dealer, cardstack)
    dealervalue = printhand(dealer)
    for x in range(hands + 1):
        if hands > 0:
            print("Hand ", x + 1, ":")
        if handvalue[x] > 21:
            print("You lost")
            tokens -= bet[x]
        elif dealervalue > 21:
            print("Dealer busted\nYou won")
            tokens += bet[x]
        elif handvalue[x] == dealervalue:
            print("You tied")
        elif handvalue[x] > dealervalue:
            print("You won")
            tokens += bet[x]
        else:
            print("You lost")
            tokens -= bet[x]
    print("Tokens: ", tokens, "\nPlay again? Yes or No")
    loopchoice = input()
    if loopchoice == "No" or loopchoice == "no" or loopchoice == "N" or loopchoice == "n":
        loop = False
