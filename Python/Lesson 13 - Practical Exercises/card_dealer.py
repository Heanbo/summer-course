# Write a program that contains all 52 standard playing cards in a data structure 
# of your choice. After prompting, a random card is dealt to the user and it prints 
# to the screen and is removed from the deck. The program should cycle through all 52 
# cards before it resets the deck again. The user should be able to quit by typing 'exit'.

import random

# 1.  TODO Define the suits and ranks for cards in two lists of strings.


# 2.  TODO Make a function that creates a deck. It should return a list of 52 strings.
#     HINT: Iterate over the suits and iterate over ranks inside that loop. 


# 3.  TODO Create a new deck.


# 4.1 TODO Create continuous loop with prompt to deal card or exit (type '+' or 'exit').
# 4.2 TODO If '+' inputted, check deck length. If length is 0, create a new deck.
# 4.3 TODO Generate a random card from the deck, print it, and remove it from the deck.
#     HINT: Use random.choice(list())   