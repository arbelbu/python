import random

for n in range(4):
    while n>5:
        cp=random.randint(1,4)
        np=input(" Give number between 0 to 4\n")
        if np!=cp:
            print ("You guessed right!!!")
        elif np==cp:
            print("the computer choose",cp,"\ntry again\n")
