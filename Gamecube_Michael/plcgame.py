def plc():
    plcscore = 0
    print("\n1: Programs, logic and controller\n2: Portable logic controller\n3: Playable logic controller\n4: Programmable logic controller\n")
    Quest1 = input("\nPress a number between 1.. 4 but be carefull\n\nWe would'nt want you to go back, would we?\n")

    #while loop if the users answer is wrong
    while Quest1 != '4':
        print("\nWrong mortal")
        #subtraction to the users score if incorrect answer
        plcscore -= 1
        Quest1 = input("\nTry again, but accept you fate and lose a point\n")
    #else statement to print what happens if the answer is correct
    else:
        #1 addition to the users score if correct answer
        plcscore += 1

    print("\nThat is correct, you may step forward\n\nI have this PLC lying around, but to get it programmed i need one thing\n")

    print("\n1: Console\n2: Programming helper\n3: Programming unit\n")

    #second quest for the user
    Quest2 = input("\nYou have to take the right one, or you won't be able to program it\n")
    
    #while loop nr 2 for the second question
    while Quest2 != '3':
        print("\nYou must be better than this, i will now deduct points for this betrayal!")
        Quest2 = input("\nTry again, don't fail, you don't want me to be disappointed\n")
        plcscore -= 1
    else:
        plcscore += 1
        print("\nLooking good human, lets move on\n\nTo get moving on, we need to program it\nTo program it we will use Structered text")

    return plcscore
    
