# to be worked on later because i need to refigure it out
# needed components: word/phrase list, guess counter, game loop
import random

# words/phrases will be pulled from here
word_list = ["JOHN EGBERT", "ECTOBIOLOGIST", "LAND OF WIND AND SHADE", "HAMMER", "HEIR", "BREATH", "NANA"]
remaining_guesses = 6

def random_word(list):
	return list[random.randint(0, len(list))]

def new_display():
	word = ""
	
	for i in word_to_guess:
		if i != " ":
			word += "_"
		else:
			word += " "
			
	return word

word_to_guess = random_word(word_list)
display_word = new_display()
incorrect_letters = []

print(display_word)

while remaining_guesses > -1:
	display_word = list(display_word)
	check_against = list(word_to_guess)
	guess = input("Letter: ").upper()
	
	#checks to see if the letter guessed is in the word
	if guess in check_against:
		for i in range(len(check_against)):
			if guess == check_against[i]:
				display_word[i] = guess
	elif len(guess) > 1:
		print("Please only select one letter")
		continue
	else:
		remaining_guesses -= 1
		incorrect_letters.append(guess)
	
	#updates player on if they guessed right or not
	display_word = "".join(display_word)
	print(display_word)
	print(incorrect_letters)
	
	#loss message and resetting the game
	if remaining_guesses == 0:
		play = input("You lost... Play again? (Y to continue)" )
		if play.upper() == "Y":
			remaining_guesses = 6
			word_to_guess = random_word(word_list)
			display_word = new_display()
			incorrect_letters = []
			
			print(display_word)
		else:
			remaining_guesses = -1;
	
	#victory message and resetting the game
	if display_word == word_to_guess:
		play = input("You won!!! Play again? (Y to continue)" )
		if play.upper() == "Y":
			remaining_guesses = 6
			word_to_guess = random_word(word_list)
			display_word = new_display()
			incorrect_letters = []
			
			print(display_word)
		else:
			remaining_guesses = -1