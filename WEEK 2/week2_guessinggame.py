# Paste your code into this box
def guessing_game():
    print("Please think of a number between 0 and 100!")

    # At the start the highest the number could be is 100 and lowest 0
    low = 0
    high = 100
    guessed = False

    # Loop until guess is correct
    while not guessed:

        # Binary search: guess the midpoint between our current high and low guesses
        guess = (high + low) // 2
        print("Is your secret number", guess, "?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low." + 
                " Enter 'c' to indicate I guessed correctly.")

        print(answer)

        if answer == 'c':
            guessed = True
        elif answer == 'h':
            high = guess
        elif answer == 'l':
            low = guess
        elif answer == 'q':
            exit()
        else:
            print("Sorry, I did not understand your input.")

    print("Game over. Your secret number was: ", guess)

guessing_game()
           
