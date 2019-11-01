def robot():
    robotscore = 0
        #5th quest for the user
    print("\nWe need to get this robot to move\n")

    print("\n1: y,z axis\n2: x,y axis\n3: x,z axis\n")
    Quest5 = input("\nTo get the robot to move to the sides, then which of the axis's are the right ones?\n")

    while Quest5 != '2':
        print("\nDummy! thats not how a robot works!\n")
        Quest5 = input("\n You better get it right this time!\n")
        robotscore -= 1
    else:
        print("\nLet's move forward\n")
        robotscore += 1

    print("\nIn order to get the item, with the robotarm, you need to calculate alittle\n")
    
    #6th quest for the user
    print("\nIf the robot is 2m tall, and you need to grab a thing that is 4m away, how long does your robot arm have to be?\n")
    Quest6 = input("\nYou have to find the correct lenght with x,xx\n")

    while Quest6 != '4,47':
        print("\nThat is not correct at all, try again\n")
        Quest6 = input("\nYou have to find the correct lenght with x,xx\n")
        robotscore -= 1
    else:
        print("\nCorrect, you have reached the item\n")
        robotscore += 1

    return robotscore