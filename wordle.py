## Main Wordle file for game

#import other modules such as dict and random answer


# define class Wordle

    # define __init__ method

    # define the game parameters
    # restrict to 6 attempts
    # make sure the word is 5 letters long and is in the dictionary


    # define the guessing method

class Wordle:
    # Main class for the Wordle game, takes arguments and checks against dictionary.
    def __init__(self, word: str = 'hello', enforce_length: bool = True, real_word: bool = True, random_daily: bool = False):
        # Add better description here
        self.word = word.upper()
        self.enforce_length = enforce_length
        self.real_word = real_word
        if random_daily:
            self.word = randomanswer.random_word(daily=True).upper()

        # Track number of guesses
        self.guesses = []

   
                
            





      