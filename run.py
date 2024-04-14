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