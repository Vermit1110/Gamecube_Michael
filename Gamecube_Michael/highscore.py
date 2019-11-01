#opens the highscore list
def highscorelist():
    f = open("highscore.txt", "r+")
    print(f.read().splitlines())
