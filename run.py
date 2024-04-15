import random
from words import word_list 
from hangman_stages import display_hangman

# Function to get a random word from the word list
def get_word():
    word = random.choice(word_list)
    # Convert the word to uppercase for consistency
    return word.upper()  


# Get a random word and print it
random_word = get_word()
print("Random word:", random_word)

# Print initial message
print("Welcome to Hangman!")


# Function that prompts the user for input to determine if they want to read the instructions:
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

# Call the function to check if the user wants to read the instructions
read_instructions()

# Call the function to display the default stage of the hangman
print(display_hangman(0))

# Function to start the game
def start_game(word):
    # Initialize variables
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    word_completion = "_" * len(word)
    game_over = False
    
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
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print(display_hangman(incorrect_guesses))
        
        # Check if the player has won
        if "_" not in word_completion:
            print("Congratulations! You've guessed the word:", word)
            game_over = True
        # Check if the player has lost
        elif incorrect_guesses == max_attempts:
            print("Sorry, you've run out of attempts. The word was:", word)
            game_over = True

# Start the game with the random word
start_game(random_word)
