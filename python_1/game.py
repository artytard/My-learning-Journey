import random

# Function to run a single guessing round and track the player's guesses
def play_round():
    # Chooses a fresh random number and sets up tracking variables for the round
    number = random.randint(1, 1000)
    guesses = []  # List to store every guess made during this round
    round_won = False  # Boolean (third data type) to track if the round is finished
    
    print("I'm thinking of a number between 1 and 1000.")

    # Inner loop runs while the player has not won yet
    while not round_won:
        guess = int(input("Enter your guess: "))
        guesses.append(guess)  # Adds the current guess to the list

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            round_won = True  # Updates the boolean to end the inner loop
            print(f"You won! 🎉 It took you {len(guesses)} guesses.")
            
            # Loop through the list of guesses to display them back to the player
            print("Here is a summary of your guesses:")
            for past_guess in guesses:
                print(f"- {past_guess}")


print("🎮 Welcome to Guess the Number!")

# Outer loop to handle restarting the entire game
while True:
    play_round()  # Calls the function to start a new guessing round

    # Ask the user if they want to play another round
    # .strip().lower() handles spaces and capital letters (e.g., "Yes ", "YES", "yEs")
    play_again = input("\nDo you wanna play again? (yes/no): ").strip().lower()
    
    if play_again != "yes":
        print("It was fun playing with you:) 🎮")
        break  # Breaks the outer loop to end the program
