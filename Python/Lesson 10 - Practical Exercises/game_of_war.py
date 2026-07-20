# Create a program that randomly deals the player and an NPC 26 cards each totaling 
# a standard deck. After the cards are dealt, begin a new round each time the user 
# inputs `+` to display the top card from each player's deck and award a point to the 
# player with the highest numeric card (Ace = 1, King = 13, Queen = 12, Jack = 11). 
# In the case cards of equal value are drawn, both players immediately draw again until 
# one side draws a card of greater numeric value (or both players exhaust their deck). 
# Once all cards are exhausted print a message to the screen honoring the winner of the 
# game or announcing a tie. The player can forfeit the game at any time by typing `exit`.


import random

# 1.1 TODO Define the suits and ranks for cards in two lists of strings.
# 1.2 TODO Create a dictionary that defines the numeric value of each rank.
#     HINT: "A": 1, "2": 2, ... "Q": 12, "K": 13


# 2.1 TODO Create a deck. It should be a list of 52 tuples (rank, suit).
#     HINT: Iterate over the suits and iterate over ranks inside that loop. 
# 2.2 TODO Shuffle and deal the deck.
#     HINT: Use random.shuffle(list()) and list subsets to split it. 
# 2.3 TODO Initialize the player and NPC scores. Print a greeting.


# 3.1 TODO Create a continuous loop that escapes when either player's deck is empty.
#     NOTE TODOs 3.2 - 7.3 are written inside this loop.
# 3.2 TODO Prompt for user input of 'exit' or '+'. 
# 3.3 TODO If input equals 'exit', print a goodbye message and escape the loop.
# 3.4 TODO If input equals anything except '+', return to the beginning of the loop.


# 4.1 TODO Draw a card from the top of each player's deck.
#     HINT: list().pop()
# 4.2 TODO Print a message displaying the player's card versus the NPC's card.


# 5.  TODO Store the values of the player and NPC's card in two ints.
#     HINT: The first index of the card tuple is the rank, use the dictionary
#           we made earlier to assess the numeric value of a rank.


# 6.1 TODO Create a continuous while loop to handle ties (ie. PC Rank = NPC Rank).
# 6.2 TODO Print a message denoting "War!".
# 6.3 TODO Create a condition that if either player's deck is empty the loop escapes.
# 6.4 TODO Draw a new card for each player. 
# 6.5 TODO Store the corresponding values of the new cards to the appropriate ints.
# 6.6 TODO Print a message displaying the player's card versus the NPC's card.
#     NOTE We are done with this loop, it will iterate as many times as it needs
#          to until a tie is resolved.


# 7.1 TODO Compare whose card value is higher using the appropriate ints you assigned.
# 7.2 TODO Award the victor a point and print a message announcing who won the round. 
# 7.3 TODO Display the total score so far for the game.


# 8.1 TODO Outside of the previous loop, announce the game has ended.
#     NOTE The condition that at least one player is out of cards has been met.
# 8.2 TODO Compare the scores of each player and announce the winner or a tie.