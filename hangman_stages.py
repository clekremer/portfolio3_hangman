# Function to display the hangman based on number of tries left
def display_hangman(tries):
    # ASCII art for the different stages of the hangman
    stages = [

        """
           _________
            |/
            |
            |
            |
            |
            |
            |___
            """,
        """
           _________
            |/   |
            |
            |
            |
            |
            |
            |___
            H""",

        """
           _________
            |/   |
            |   (_)
            |
            |
            |
            |
            |___
            HA""",

        """
           _________
            |/   |
            |   (_)
            |    |
            |    |
            |
            |
            |___
            HAN""",

        """
           _________
            |/   |
            |   (_)
            |   /|
            |    |
            |
            |
            |___
            HANG""",

        """
           _________
            |/   |
            |   (_)
            |   /|\\
            |    |
            |
            |
            |___
            HANGM""",

        """
           _________
            |/   |
            |   (_)
            |   /|\\
            |    |
            |   /
            |
            |___
            HANGMA""",

        """
           _________
            |/   |
            |   (_)
            |   /|\\
            |    |
            |   / \\
            |
            |___
            HANGMAN"""]
    # Return the corresponding stage of the hangman
    return stages[tries]
