"""
This is a simple hangman game where the user has to guess the food.
"""

# Imports
import random
import wordsforhangman

# Variables
words = wordsforhangman.words
answer = random.choice(words)
blanks = ['_'] * len(answer)
attempts = 6
guessed_letters = set()

# Game
print('****************************************')
print(f'{"Welcome to the Hangman Game!" :^40}')
print(f'{"All words are related to foods." :^40}')
print(f'{"You have 6 incorrect guesses. Good luck." :^40}')
print('****************************************')
print()

print(' '.join(blanks))

while attempts > 0 and '_' in blanks: # Runs while the attempts are greater than 0 and there are still blanks.
    guess = input('Enter your guess: ').lower()
    
    if guess in guessed_letters: # Checks if user has already guessed the letter.
        print('You have already guessed that letter. Try again.\n')
        continue
    
    guessed_letters.add(guess)
    
    if guess in answer: # Checks if the guess is in the answer.
        for index, letter in enumerate(answer): # Iterates over each letter in the answer, collecting the index.
            if letter == guess:
                blanks[index] = guess # Replaces the blank with the guess.
    else:
        attempts -= 1
        print(f'Wrong guess. You have {attempts} attempts left.')
    
    print()
    print(' '.join(blanks))

# End Of Game
if '_' not in blanks:
    print(f'Congratulations! You guessed the word: {answer}.')
else:
    print(f'Sorry, you ran out of attempts. The word was: {answer}.')
