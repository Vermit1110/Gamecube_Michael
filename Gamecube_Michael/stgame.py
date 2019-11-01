def st():
    stscore = 0
#3rd quest for the user
    print("\n1: Timer\n2: Ton\n3: Time\n4: Toh")
    Quest3 = input("\nWhich of the above statements do i need, to create a timer for my program?\n")
    stscore = 0
    while Quest3 != '2':
        print("\nYou disappoint me, Thanks for the points!\n")
        Quest3 = input("\nYou may try again, i want more of these points of yours\n")
        stscore -= 1
    else:
        stscore += 1
        print("\nYou came this far, now lets move forward\n")

#4th quest for the user
    print("\nI need to make a function for this program.\n")

    print("\n\n1: Function_block <name>\n2: FC <name>\n3: Function <name>\n4: <name> Function\n")
    Quest4 = input("\nWhich of the above statements is the right one, to create a function?\n")
    
    while Quest4 != '3':
        print("\nYou have to shape up, if you want to continue this journey!")
        Quest4 = input("\nTry again, but do it right this time...\n")
        stscore -= 1
    else:
        stscore += 1
        print("\nYou are getting better... i guess\n")

    return stscore
