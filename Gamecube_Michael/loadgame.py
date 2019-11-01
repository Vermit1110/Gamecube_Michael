#import pickle
def loadagame(namevar):
    username = input(str("insert name "))
    f = open("save.txt", "r")
    f.readlines([namevar, ", ", str(point),", ", "position", "\n"])
    for i in f:
        if username == f.readline([namevar]):
            print(username)
    f.close()

