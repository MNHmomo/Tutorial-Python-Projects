name = input("Type your name: ")
print( "Welcome", name, "to this adventure!")

answer = input ("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come across a river, you can either walk around it or swim across it. Type 'walk' to walk around the river, or 'swim' to swim across it: ").lower()

    if answer == "swim":
        answer = input("You swam across and were spotted by an alligator. He charges at you, and you can either choose to fight back or flee. Type 'fight' to fight the alligator, or 'flee' to swim away: ").lower()
        if answer == "fight":
            print("You chose to fight the alligator, but it was a horrible idea. You end up bleeding out from the bites inlicted upon you.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        elif answer == "flee":
            print("You attemp to swim away, but the alligator is far too fast for you. You end up bleeding out from the bites inflicted upon you.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        else:
            print("Not a valid option. You Lose.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
    elif answer == "walk":
        answer = input("You walk for miles looking for a way around the river. You become extemely thristy, and the only water source is the river beside you. Do you drink the river water or continue to walk? Type 'drink' to drink the river water, or 'walk' to continue walking:  ").lower()
        if answer == "drink":
            print("You have gotten severly ill from the river water, and eventually die.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        elif answer == "walk":
            print("You have long past the river and end up walking for miles, never finding any available water souce. You eventually die of thrist.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        else:
            print("Not a valid option. You Lose.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
    else:
        print("Not a valid option. You Lose.")
        answer = input("Type 'Q' to admit you lost: ").lower()
        if answer == "Q":
                quit()

elif answer == "right":
    answer = input("You see a shed with an open door. Do you enter or leave it alone? Type 'enter' to enter the shed, or 'leave' to leave it alone and continue walking: ").lower()

    if answer == "enter":
        answer = input("You enter the shed and get ambushed by a stranger. He demands money from you, do you give it to him or refuse? Type 'give' to give him the money, or 'refuse' to deny his demand: ").lower()
        if answer == "give":
            print("The stranger snatches the money and stabs you anyway, in hopes of no witnessess. You end up bleeding out from the stab wounds inflicted upon you.right")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        elif answer == "refuse":
            print("The stranger does not like your answer. You end up bleeding out from the stab wounds inflicted upon you.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        else:
            print("Not a valid option. You Lose.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
    elif answer == "leave":
        answer = input("You leave the shed alone, and get a feeling that you have avoided danger. Continuing your walk, you stumble across a panther who is bloodthristy. Do you fight and defend yourself, or retreat an find cover. Type 'fight' to figth the panther, or 'retreat' to run away: ").lower()
        if answer == "fight":
            print("The panther is far more powerful than you. You end up bleeding out from the bites inflicted upon you.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        elif answer == "retreat":
            print("The panther is far more faster than you are. You end up bleeding out from the bites inflicted upon you.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
        else:
            print("Not a valid option. You Lose.")
            answer = input("Type 'Q' to admit you lost: ").lower()
            if answer == "Q":
                quit()
else:
    print("Not a valid option. You Lose.")
    answer = input("Type 'Q' to admit you lost: ").lower()
    if answer == "Q":
                quit()
