import random
correctAnsewer = random.randint(1,9)
gameOver = False

while gameOver == False:

    playerGuess=int(input("Guess a number between 1 and 9: "))

    if playerGuess == correctAnsewer:
        compareAnsewer = "Right"
        gameOver = True
    elif playerGuess > correctAnsewer
        compareAnsewer = "High"
    elif playerGuess < correctAnsewer:
        compareAnsewer = "Low"

    if compareAnsewer == "Right":
        print("Correct! You Win!")
    elif compareAnsewer == "High":
        print("Too High! Guess Again!")
    elif compareAnsewer == "Low":
        print("Too Low! Guess Again!")