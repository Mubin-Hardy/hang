import random
def hangman():
    word = random.choice(["pugger","littlepugger","tiger","superman","avengers","savewater","anabelle"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade=""
    replay = ""
    while len(word)> 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_"+" "
        if main == word:
            print(main)
            print("you win")
            break
        print("guess the word:",main)
        guess = input()
        if guess in validletters:
            guessmade = guessmade + guess
            print("guesss made ==",guessmade)
        else:
            print("enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("----------")
                print("     O     ")
            if turns == 8:
                print("8 turns left")
                print("----------")
                print("     O_    ")
            if turns == 7:
                print("7 turns left")
                print("----------")
                print("    _ O_       ")
            if turns == 6:
                print("6 turns left")
                print("----------")
                print("    _ O_   ")
                print("      |     ")
            if turns == 5:
                print("5 turns left")
                print("----------")
                print("    _ O_   ")
                print("      |     ")
                print("     /       ")
            if turns == 4:
                print("4 turns left")
                print("----------")
                print("    _ O_   ")
                print("      |     ")
                print("     / |      ")
            if turns == 3:
                print("3 turns left")
                print("----------")
                print("    _ O_   ")
                print("      |     ")
                print("     / |       ")
            if turns == 2:
                print("2 turns left")
                print("----------")
                print("    [_ O_   ")
                print("      |     ")
                print("     / |       ")
            if turns == 1:
                print("1 turn left")
                print("----------")
                print("    [_ O_]   ")
                print("      |     ")
                print("     / |       ")
            if turns == 0:
                print("you loose")
                print("you let the kind man die")
                print("--------|----")
                print("    [_ O|_]       ")
                print("        |          ")
                print("        |       ")
                print("       / |        ")
                print("             ")
                print("enter y to try again and n to exit")
                replay = input()
                if replay == "y":
                    hangman()
                    if replay == "n":
                        break
                    else:
                        replay = input("enter a valid y or n  ")


name = input("enter your name")
print("welcome", name)
print("------------------------------")
print("try to guess the word in only 10 attempts")
hangman()
print()
