# Hands-On: Practical Exercises

This repository is designed to reinforce the knowledge already learned in previous lessons and apply it towards practical exercises that can measure learning.


## 🎯 Lesson Objectives

* Create a Calculator
* Mine AI2Coin
* Build a Card Dealer
* Game of War

---

### Exercise 1: 🧮 Create a Calculator

**Goal**: Write a program that accepts a simple mathematical expression as input, evaluates the expression, and displays the resulting solution to the user. 

✅ *Check*: Output should accept input as two numbers separated by spaces and an operator (eg. `6 - 8`) and the evaluated expression (eg. `6 - 8 = 2`) should be printed to the terminal.

---

### Exercise 2: 🪙 Mine AI2Coin

**Goal**: Write a program that calculates however many semiprime numbers (the product of two prime numbers) the user specifies and prints them to the screen.

✅ *Check*: User is able to input `10` and screen outputs 10 different semi prime numbers starting from 4 (eg. `4 6 9 10 14 15 21 22 25 26`). 

---

### Exercise 3: 🂡 Build a Card Dealer

**Goal**: Write a program that contains all 52 standard playing cards in a data structure of your choice. After prompting, a random card is dealt to the user and it prints to the screen and is removed from the deck. The program should cycle through all 52 cards before it resets the deck again. The user should be able to quit by typing 'exit'.

💩 *Emojidex*: ♠ ♣ ♥︎ ♦

✅ *Check*: User is able to input `+` and screen outputs something like `K♥︎` followed by `A♣` upon another `+` inputted. Typing `exit` results in the program ceasing. 

---

### Exercise 4: ⚔️ Game of War

**Goal**: Create a program that randomly deals the player and an NPC 26 cards each totaling a standard deck. After the cards are dealt, begin a new round each time the user inputs `+` to display the top card from each player's deck and award a point to the player with the highest numeric card (Ace = 1, King = 13, Queen = 12, Jack = 11). In the case cards of equal value are drawn, both players immediately draw again until one side draws a card of greater numeric value (or both players exhaust their deck). Once all cards are exhausted print a message to the screen honoring the winner of the game or announcing a tie. The player can forfeit the game at any time by typing `exit`. 

💩 *Emojidex*: ♠ ♣ ♥︎ ♦

✅ *Check*: Cards are dealt to the user and an NPC, user is able to input `+` to initiate a round and screen outputs something like `K♥︎  x  6♣` followed by a new line announcing `Player wins this round!`. Scores are updated after each round, in this case displaying `Player: 1  | Opponent: 0`. Typing `exit` results in the screen displaying `Player loses by forfeit!` the program ceasing. 

