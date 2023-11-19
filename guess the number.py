actual_number = 25
attempts = 0

while True:
    attempts += 1
    guess = int(input("Guess the number:\n"))
    if guess < actual_number:
        print("your guess is to low")

    elif guess > actual_number:
        print("Your guess is to high")

    else:
        print(f"You guessed the numberr in {attempts} attempts")
        break
print("thanks for playing!")
