import random

n = random.randint(1, 100)

level = input("Which level you want to play?'Easy' or 'Hard'.\n").lower()

if level == 'easy':
    guesses = 10
else:
    guesses = 5

game_on = True

while game_on:
    print(f"You have {guesses} guesses remaining.")
    guessnum = int(input("Make a guess :\n"))
    if guesses == 0:
        game_on = False
        print("You have no guesses left. You lose.")
        print(f"The correct answer was {n}")
    elif guessnum == n:
        game_on = False
        print("You guessed it right:")
    elif guessnum > n:
        print("Too high.")
        guesses -= 1
    elif guessnum < n:
        print("Too low.")
        guesses -= 1
