from random import randint

for x in range(1,10):
    guessnumber = int(input("Enter your guess between 1 to 5: "))
    randomNumber = randint(1,3)
    if guessnumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was: ",randomNumber)