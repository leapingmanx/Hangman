# to be worked on later because i need to refigure it out
# needed components: word/phrase list, guess counter, game loop
import random
import time

# words/phrases will be pulled from here
word_list = ["JOHN EGBERT", "ECTOBIOLOGIST", "LAND OF WIND AND SHADE", "HAMMER", "HEIR", "BREATH", "NANA"]
remaining_guesses = 6

def random_word(list):
	return list[random.randint(0, len(list))]

word_to_guess = random_word(word_list)
display_word = ""

for i in word_to_guess:
	if i != " ":
		display_word += "_"

incorrect_letters = []

print(display_word)

time.sleep(5)