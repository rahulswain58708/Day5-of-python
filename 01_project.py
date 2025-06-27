#NUMBER GUESS GAME
import random
#step 1: Generate a random number between 1 to 100
secret_number=random.randint(1,100)
#step 2: set the maximum number of attempt
attempts=7
print("Welcome to the number guessing game!")
print("Guess The number between 1 and 100")
print(f"you have {attempts}attempts.Good luck!\n")
#step 3: loop for attempts
for i in range(1,attempts+1):
    guess=int(input(f" attempt{i}: Enter youur guess : "))

    if guess==secret_number:
        print(f"congratulation! you guess it in {i} attempts.")
        break
    elif guess<secret_number:
        print("Too Low!")
    else:
        print("Too high")
        if i==attempts:
            print(f"out of attempts ! The correct number was {secret_number}")

      