
print("      " + "*" * 19,end='\n'"      " +"|" + " Welcome Stranger" + " |"'\n'"      " + "*" * 19)
print("\n|" + " Step into my lair, but be prepared |")
print("\nYour first assignment is to assemble some parts to my PLC\n\nFirst you need to know what a PLC is\n")

    #First quest. User inputs an answer to the question
def q1(username, score):
    score = 10
    print("\n1: Programs, logic and controller\n2: Portable logic controller\n3: Playable logic controller\n4: Programmable logic controller\n")
    Quest1 = input("\nPress a number between 1.. 4 but be carefull\n\nWe would'nt want you to go back, would we?\n")

    #while loop if the users answer is wrong
    while Quest1 != '4':
        print("\nWrong mortal")
        #subtraction to the users score if incorrect answer
        score -= 1
        Quest1 = input("\nTry again, but accept you fate and lose a point\n")
    #else statement to print what happens if the answer is correct
    else:
        #1 addition to the users score if correct answer
        score += 1
    svgame = input(" Save game? Yes or No: ")
    if svgame == "yes":
        savegame(username, score, "Quest2")

    Quest2(Point, username)
    print("\nThat is correct, you may step forward\n\nI have this PLC lying around, but to get it programmed i need one thing")

    print("\n1: Console\n2: Programming helper\n3: Programming unit")

    #second quest for the user
    Quest2 = input("\nYou have to take the right one, or you won't be able to program it\n")
    
    #while loop nr 2 for the second question
    while Quest2 != '3':
        print("\nYou must be better than this, i will now deduct points for this betrayal!")
        Quest2 = input("\nTry again, don't fail, you don't want me to be disappointed\n")
        score -= 1
    else:
        score += 1
        print("\nLooking good human, lets move on\n\nTo get moving on, we need to program it\nTo program it we will use Structered text")

    #3rd quest for the user
    print("\n1: Timer\n2: Ton\n3: Time\n4: Toh")
    Quest3 = input("\nWhich of the above statements do i need, to create a timer for my program?\n")

    while Quest3 != '2':
        print("\nYou disappoint me, Thanks for the points!")
        Quest3 = input("\nYou may try again, i want more of these points of yours\n")
        score -= 1
    else:
        score += 1
        print("\nYou came this far, now lets move forward")
    
    #4th quest for the user
    print("\nI need to make a function for this program.")

    print("\n\n1: Function_block <name>\n2: FC <name>\n3:Function <name>\n4: <name> Function\n")
    Quest4 = input("\nWhich of the above statements is the right one, to create a function?\n")
    
    while Quest4 != '3':
        print("\nYou have to shape up, if you want to continue this journey!")
        Quest4 = input("\nTry again, but do it right this time...\n")
        score -= 1
    else:
        score += 1
        print("You are getting better... i guess")
    
    #5th quest for the user
    print("\nWe need to get this robot to move")

    print("\n1: y,z axis\n2: x,y axis\n3: x,z axis")
    Quest5 = input("\nTo get the robot to move to the sides, then which of the axis's are the right ones?\n")

    while Quest5 != '2':
        print("Dummy! thats not how a robot works!")
        Quest5 = input("\n You better get it right this time!\n")
        score -= 1
    else:
        print("\nLet's move forward")

    print("\nIn order to get the item, with the robotarm, you need to calculate alittle")
    
    #6th quest for the user
    print("\nIf the robot is 2m tall, and you need to grab a thing that is 4m away, how long does your robot arm have to be?")
    Quest6 = input("\nYou have to find the correct lenght with x,xx\n")

    while Quest6 != '4,47':
        print("That is not correct at all, try again")
        Quest6 = input("You have to find the correct lenght with x,xx\n")
        score -= 1
    else:
        print("\nCorrect, you have reached the item")

    #a little hangman game for the user, as a break from the real game
    print("\n\n You reached this far, now time for a little break for you, with this little game of hangman, lets see how good you are\n")
    nextgame = input("\nPress 1 to go to the hangman game, or press 2 if you want to continue on your adventure")
    if nextgame == "1":
        import Hangmangame
    if nextgame == "2":
        print("\nNow lets continue")
    else:
        nextgame = input("\nPress 1 to go to the hangman game, or press 2 if you want to continue on your adventure")
    
        print("now its time to test your knowledge in Python")

    #7th quest to get the user to define a function in python, having to write 2 statements
    print("\nIf you want a function to store a value to the function, how should you write it?")
    print("\n ___ myfuntion()\n ______")
    firstinp = input("\nfirst word: ")
    
    while firstinp != 'def':
        print("\nIncorrect")
        firstinp = input("\nfirst word:___ ")
        score -= 1
    else:
        print("\nCorrect")
    if firstinp == "def":
        secondinp = input("\nsecond word: ")
    while secondinp != 'return':
        print("\nIncorrect")
        secondinp = input("\nsecond word: ")
        score -= 1
    else:
        print("\nCorrect")
        score += 1

    print("\nNow i want a list to my python program, and i need you to help me\nI need a list with 3 variables respectively: 85, 34, 90")
    Quest8 = input("You need to create the list after 'mylist = ___\n")

    while Quest8 != '[85, 34, 90]':
        print("\nThat is not the way to go")
        Quest8 = input("\nYou need to create the list after 'mylist = ___\n")
        score -= 1
    else:
        print("\nThat is correct!\nYou finished thhe game, you will be sent back to the menu")
        score += 1
        import GameCube_Michael

def savegame(username, point, position):
    print("\nsavegame ", point, " points ", position)
    
    f = open("Username.txt", "a")
    f.writelines([username, ", ", str(point),", ", position, "\n"])
    f.close()

    return