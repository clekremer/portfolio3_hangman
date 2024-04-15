import random
from words import word_list 
from hangman_stages import display_hangman
from pyfiglet import figlet_format
import os

# Function to get a random word from the word list
def get_word():
    word = random.choice(word_list)
    # Convert the word to uppercase for consistency
    return word.upper()  

# Function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display instructions
def read_instructions():
    while True:
        choice = input("Do you want to read the instructions? (Y/N): ").strip().upper()
        if choice == 'Y':
            print("Instructions:")
            print("1. A random word has been selected.")
            print("2. You have to guess the letters in the word.")
            print("3. You can only make 6 incorrect guesses before losing.")
            print("4. Good luck!")
            break
        elif choice == 'N':
            print("Alright! Let's start the game.")
            break
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")

# Function to start the game
def start_game(word):
    # Initialize variables
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 7
    word_completion = "_" * len(word)
    game_over = False
    
    # Display initial hangman stage
    print(display_hangman(0))
    
    # Main game loop
    while not game_over:
        print("\nWord to guess:", word_completion)
        print("Used letters:", ", ".join(guessed_letters))  # Display used letters
        guess = input("Guess a letter: ").upper()
        
        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word:
            print("Correct guess!")
            # Update the word completion with the correctly guessed letter
            word_completion = "".join([char if char in guessed_letters else "_" for char in word])
            print("\nWord to guess:", word_completion)  # Display updated word completion
            print(display_hangman(incorrect_guesses))  # Display current hangman stage
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print(display_hangman(incorrect_guesses))  # Display current hangman stage
        
        # Check if the player has won
        if "_" not in word_completion:
            print(figlet_format("WON", font="acrobatic"))
            print("Congratulations! You've guessed the word:", word)
            return True
        # Check if the player has lost
        elif incorrect_guesses == max_attempts:
            print(figlet_format("LOSE", font="acrobatic"))
            print("Sorry, you've run out of attempts. The word was:", word)
            return False

# Function to restart the game
def restart_game():
    while True:
        play_again = input("Do you want to play again? (Y/N): ").strip().upper()
        if play_again == 'Y':
            return True
        elif play_again == 'N':
            print(figlet_format("Goodbye", font="acrobatic"))
            print("Thank you for playing!")
            return False
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")

# Main game loop
while True:
    # Print initial message
    print(figlet_format("Hangman", font="acrobatic"))
    
    # Call the function to check if the user wants to read the instructions
    read_instructions()

    # Get a random word
    random_word = get_word()
    print("Random word:", random_word)

    # Start the game with the random word
    if start_game(random_word):
        # Check if the player wants to play again
        if not restart_game():
            break
    else:
        # If the player lost, ask to restart the game
        if not restart_game():
            break

    clear_terminal()
