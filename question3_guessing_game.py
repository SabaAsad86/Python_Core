
secret_number = 42
attempts = 0

while attempts < 5:
    guess = int(input("Guess a number (1-100): "))

    if guess < 1 or guess > 100:
        print("Invalid number! Try again.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Congratulations! Correct guess.")
        break
    else:
        print("Wrong guess! Try again.")

else:
    print("Game Over! You lost.")
