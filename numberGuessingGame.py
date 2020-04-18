from random import randint
def difficutlty(level, range):
    points = 0
    guesses = level
    while guesses > 0:
        computer = randint(1, range)
        user = input("Enter your guess \n>")
        if user.isalpha():
            print(f"Sorry, '{user}' is not a valid number")
        else:
            if int(user) == computer:
                points += 3
                print(f"You got it right! points = {points}")
            else:
                guesses -= 1
                print(f"That was wrong! Remaining Guesses = {guesses}")
                if guesses == 0:
                    print(f"Game over! Total Points = {points}")
                    points = 0

while True:
    stage = input("\nEnter difficulty level ( 'easy, medium or hard' ) to end game type 'quit'\n>")
    if stage.lower() == "easy":
        difficutlty(6, 10)
    elif stage.lower() == "medium":
        difficutlty(4, 20)
    elif stage.lower() == "hard":
        difficutlty(3, 50)
    elif stage.lower() == "quit":
        print("Shutting down....End")
        break
    else:
        print(f"'{stage}' is not a valid input \n")
        