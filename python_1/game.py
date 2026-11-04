import random

print("🎮 Welcome to Guess the Number!")

# Outer loop to handle restarting the entire game
while True:
    # Chooses a fresh random number and resets attempts for the new round
    number = random.randint(1, 1000)
    attempts = 0
    
    print("\nI'm thinking of a number between 1 and 1000.")

    # Inner loop for the current guessing round
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"You won! 🎉 It took you {attempts} guesses.")
            break  # Breaks the inner loop when the user wins

    # Ask the user if they want to play another round
    # .strip().lower() handles spaces and capital letters (e.g., "Yes ", "YES", "yEs")
    play_again = input("\nDo you wanna play again? (yes/no): ").strip().lower()
    
    if play_again != "yes":
        print("It was fun playing with you:) 🎮")
        break  # Breaks the outer loop to end the program
