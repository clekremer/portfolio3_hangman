import random
from words import word_list 

# Function to get a random word from the word list
def get_word():
    word = random.choice(word_list)
    # Convert the word to uppercase for consistency
    return word.upper()  


# Get a random word and print it
random_word = get_word()
print("Random word:", random_word)