# This is my attempt at the hangman game version 1
import sys

import random

names = ['richard', 'rene', 'lello', 'katy', 'michael', 'theo', 'luca', 'sarah']
print('Welcome to the hangman name game!')
word = random.choice(names)  # This picks a random word from the names list
word_list = []  # This will create the empty list to add the random choice to for iteration

# This for loop puts the letters of the word into a list
for i in word:
	word_list.append(i)
#  print(f'The name is {word}')  # uncomment to debug

# We need to create a list for the guess with empty characters to show the contestant before each guess
guess_list = []
for i in range(len(word_list)):
	guess_list.append('-')
no_of_lives = 10
while no_of_lives > 0:
	guess = input(f'Guess a letter...                       {str(guess_list)}\n')
	if  guess in word:  # This will check if the letter is in the word and amend where necessary
		for i in range(len(word_list)):
			if word_list[i] == guess:
				guess_list[i] = guess
				print('Good guess!')	
				if guess_list == word_list:
					print(f'Congratulations you guessed the word!       {str(guess_list)}')
					sys.exit()
	else:
		no_of_lives -= 1
		print(f'Wrong... You have {no_of_lives} guesses left    {str(guess_list)}')
		
print('Game over')
