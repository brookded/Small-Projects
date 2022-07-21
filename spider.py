from random import randrange


class Card:
    suit = 0
    number = 0
    flipped = False


def createcards():
    col = 10
    row = 6
    stack = [[Card() for x in range(row)] for y in range(col)]
    shuffler = [4 for x in range(13)]
    for x in range(col):
        for y in range(row):
            if y == 5 or (x > 1 and y == 4):
                stack[x][y].flipped = True
            if not(x > 1 and y == 5):
                created = False
                while not created:
                    randnum = randrange(0, 13)
                    if shuffler[randnum] > 0:
                        stack[x][y].number = randnum + 1
                        shuffler[randnum] = shuffler[randnum] - 1
                        created = True
    return stack


def printcards(stack):
    inc = 0
    for y in range(len(stack[inc])):
        for x in range(len(stack)):
            if not stack[x][y].flipped:
                print("X", end="  ")
            else:
                if stack[x][y].number < 10:
                    print(stack[x][y].number, end=" ")
                    print(" ", end="")
                elif stack[x][y].number == 10:
                    print(stack[x][y].number, end=" ")
                elif stack[x][y].number == 11:
                    print("J", end="  ")
                elif stack[x][y].number == 12:
                    print("Q", end="  ")
                elif stack[x][y].number == 13:
                    print("K", end="  ")
        print("")
        inc = inc + 1
    print("")
    for x in range(len(stack)):
        print(x + 1, end="  ")


def movecards(spot, spot2, stack):
    if spot < 0 or spot > len(stack) or spot2 < 0 or spot2 > len(stack):
        print("One number does not match a column")
        return 0
    print(spot, " ", spot2)


cardstack = createcards()
printcards(cardstack)
print("\nPlease choose a column")
choice = int(input())
choice = choice - 1
print("Please choose where to move it")
choice2 = int(input())
choice2 = choice2 - 1
response = movecards(choice, choice2, cardstack)
