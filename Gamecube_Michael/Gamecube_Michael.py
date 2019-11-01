#My progression variable to determine which game to go to
nextgame = 1
#Start score for games
score = 0
import pickle
while True:
    print("""
                            Welcome to Michaels text adventure game

                     1: New Game        2: Highscore       3: Load Game         
    """)
    menuchoice = input("\npress one of the numbers above to continue\n")

    #menuchoice for the user to decide which tab him or her want to go to
    if menuchoice == '1':
        #input from user, to decide users name
        namevar = input(str("write username: ")).lower()

    #nextgame predefined as one, to start the first game, if user presses 1
        if nextgame == 1:
            #imports first game
            import plcgame
            #takes the score from the game, and adds it to the score in the menu
            score += plcgame.plc()
            #ask the user if a save game is wanted
            savequestion = input("do you want to save your progress press 1, press 2 to continue\n")
            #writes the savegame to a text file, if user decides to
            if savequestion == '1':
                f = open("save.txt", "a")
                f.writelines([namevar," , ", str(score), " , " "game 1" "\n"])
                f.close()
                nextgame += 1
            #elif savequestion == '2':
                
            else:
                nextgame += 1
                
        # nextgame equals '2' when the first game is done, so the user moves on to the structered text game
        # rest of lines is same as game one
        if nextgame == 2:
            import stgame
            score += stgame.st()
            savequestion2 = input("do you want to save your progress press 1, press 2 to continue\n")
            if savequestion2 == '1':
                f = open("save.txt", "a")
                f.writelines([namevar," , ", str(score), " , " "game 2" "\n"])
                f.close()
                nextgame += 1
            #elif savequestion2 == '2':
                
            else:
                print("do you want to save your progress press 1, press 2 to continue\n")
                nextgame += 1

        # nextgame equals '3' when the second game is done, so the user moves on to the robot game
        # rest of lines is same as game one
        if nextgame == 3:
            import robotgame
            score += robotgame.robot()
            savequestion3 = input("do you want to save your progress press 1, press 2 to continue\n")
            if savequestion3 == '1':
                f = open("save.txt", "a")
                f.writelines([namevar," , ", str(score), " , " "game 3" "\n"])
                f.close()
                nextgame += 1
            #elif savequestion3 == '2':
                
            else:
                print("do you want to save your progress press 1, press 2 to continue\n")
                nextgame += 1
        # a little fun game i found on the internet, to make it like some sort of break from the real game
        if nextgame == 4:
            import Hangman
            nextgame += 1

        # nextgame equals '5' when the fourth game is done, so the user moves on to the python game
        # rest of lines is same as game one
        if nextgame == 5:
            import pythongame
            score += pythongame.python()
            savequestion4 = input("do you want to save your progress press 1, press 2 to continue\n")
            if savequestion4 == '1':
                f = open("save.txt", "a")
                f.writelines([namevar," , ", str(score), " , " "game 4" "\n"])
                f.close()
                nextgame += 1
            #elif savequestion4 == '2':
              
            else:
                print("do you want to save your progress press 1, press 2 to continue\n")
                nextgame += 1

        # nextgame equals '6' then the game is finished, and the name and score of user is put in the highscore textfile
        if nextgame == 6:
            print("Game finished")
            f = open("highscore.txt", "a")
            f.writelines([namevar,", ", str(score), "\n"])
            f.close()
            
            continue

    # If user puts '2' in the menu, the highscore list will load
    elif menuchoice == '2':
        import highscore
        highscore.highscorelist()


    #elif menuchoice == '3':
    #    import user
    #    user.useri()

    # If user puts '2' in the console, the save.txt opens
    elif menuchoice == '3':
        import loadgame
        loadgame.loadagame(namevar)

    # if user does not put any of the numbers in the menu
    else:
        print("press one of the numbers above to continue")
