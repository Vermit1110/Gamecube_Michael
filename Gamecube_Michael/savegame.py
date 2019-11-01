def savegame(username, point, position):
    print("\nsavegame ", point, " points ", position)
    
    f = open("Username.txt", "a")
    f.writelines([username, ", ", str(point),", ", position, "\n"])
    f.close()

    return
