# Tower of Hanoi

def printtower(left, middle, right):
    inc = max(len(left), len(middle), len(right))
    for x in range(inc):
        if len(left) >= inc - x:
            print(left[inc - x - 1], end="  ")
        else:
            print(end="   ")
        if len(middle) >= inc - x:
            print(middle[inc - x - 1], end="  ")
        else:
            print(end="   ")
        if len(right) >= inc - x:
            print(right[inc - x - 1], end="  ")
        else:
            print(end="   ")
        print("")


def movetower(starttower, stoptower):
    if len(starttower) == 1 and starttower[0] == 0:
        print("First tower does not have any layers")
    elif len(stoptower) == 1 and stoptower[0] == 0:
        if len(starttower) == 1:
            stoptower[0] = starttower[0]
            starttower[0] = 0
        else:
            stoptower[0] = starttower.pop()
    elif starttower[len(starttower) - 1] > stoptower[len(stoptower) - 1]:
        print("First tower's top is larger than the second, try again")
    elif len(starttower) == 1:
        stoptower.append(starttower[0])
        starttower[0] = 0
    else:
        stoptower.append(starttower.pop())
    return


# Main Function
print("The goal is to move the tower from the left to the right.")
print("The numbers can only be stacked smallest to largest, moved one at a time")
loop = True
layers = 0
while loop:
    print("How many layers would you like?")
    layers = int(input())
    if layers > 0:
        loop = False
lefttower = [layers - x for x in range(layers)]
middletower = [0]
righttower = [0]
towers = [lefttower, middletower, righttower]
printtower(lefttower, middletower, righttower)
loop = True
while loop:
    fail = False
    start, stop = 0, 0
    while not fail:
        print("Choose the tower to move: Left (1), Middle (2), Right (3)")
        start = int(input())
        if start < 1 or start > 3:
            fail = False
        else:
            fail = True
    fail = False
    while not fail:
        print("Choose where to move: Left (1), Middle (2), Right (3)")
        stop = int(input())
        if stop == start or stop < 1 or stop > 3:
            fail = False
        else:
            fail = True
    movetower(towers[start - 1], towers[stop - 1])
    printtower(lefttower, middletower, righttower)
    if layers == len(righttower):
        loop = False
print("The tower has been moved to the right side! You win")
