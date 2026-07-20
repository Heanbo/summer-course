# Write a program that contains all 52 standard playing cards in a data structure 
# of your choice. After prompting, a random card is dealt to the user and it prints 
# to the screen and is removed from the deck. The program should cycle through all 52 
# cards before it resets the deck again. The user should be able to quit by typing 'exit'.


import random

# Define suits and ranks
suits = ["♠", "♣", "♥︎", "♦"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Create the deck
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    return deck

deck = create_deck()

while True:
    user_input = input("Enter '+' to deal a card or 'exit' to quit: ")

    if user_input == "exit":
        print("Goodbye!")
        break

    if user_input == "+":
        # Reset deck when empty
        if len(deck) == 0:
            print("Deck exhausted. Resetting deck...")
            deck = create_deck()

        # Choose a random card and remove it
        card = random.choice(deck)
        deck.remove(card)

        print(card)