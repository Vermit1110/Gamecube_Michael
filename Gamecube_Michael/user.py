def useri():

    username = input(str("Intast navn: "))

#tilføj fil og skriv i fil til oprettelse af Brugere.
    f = open("User.txt", "a")
    f.writelines([username, ", 0", ", q1\n"])
    f.close()

    return username, 0, "q1"