def python():

    pythonscore = 0
     #7th quest to get the user to define a function in python, having to write 2 statements
    print("\nIf you want a function to store a value to the function, how should you write it?")
    print("\n ___ myfuntion()\n ______")
    firstinp = input("\nfirst word: ")

    

    while firstinp != 'def':
        print("\nIncorrect\n")
        firstinp = input("\nfirst word:___")
        pythonscore -= 1

    else:
        pythonscore += 1
        print("\nCorrect\n")

    if firstinp == "def":
        secondinp = input("\nsecond word: ")

    while secondinp != 'return':
        print("\nIncorrect")
        secondinp = input("\nsecond word: ")
        pythonscore -= 1

    else:
        print("\nCorrect")
        pythonscore += 1

    print("\nNow i want a list to my python program, and i need you to help me\nI need a list with 3 variables respectively: 85, 34, 90\n")
    Quest8 = input("\nYou need to create the list after 'mylist = ___\n")

    while Quest8 != '[85, 34, 90]':
        print("\nThat is not the way to go\n")
        Quest8 = input("\nYou need to create the list after 'mylist = ___\n")
        pythonscore -= 1

    else:
        print("\nThat is correct!\nYou finished thhe game, you will be sent back to the menu")
        pythonscore += 1

    return pythonscore
