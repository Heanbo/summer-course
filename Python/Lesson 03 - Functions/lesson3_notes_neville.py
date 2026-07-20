#Lesson 3 Class Notes
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)


# computer_choice = "rock"
# user_choice = input("Enter rock, paper, or scissors:  ")

# if user_choice == "rock" and computer_choice == "paper":
#     print("You Lose")
# elif user_choice == "rock" and computer_choice == "scissors":
#     print("You Win")
# elif user_choice == "paper" and computer_choice == "scissors":
#     print("You Lose")
# elif user_choice == "paper" and computer_choice == "rock":
#     print("You Win")
# elif user_choice == "scissors" and computer_choice == "rock":
#     print("You Lose")
# elif user_choice == "scissors" and computer_choice == "paper":
#     print("You Win")
# else:
#     print("You tie")


# import random

# random_number = random.randint(1,100)
# user_number = int(input("Enter a number between 1 and 100: "))
# count = 0
# num_guesses = 0
# while user_number != random_number and num_guesses < 5:
#     if user_number > random_number:
#         print("You guessed too high")
#     else:
#         print("You guessed too low")
#     user_number = int(input("Enter a number between 1 and 100: "))
#     count += 1
#     num_guesses += 1

# if num_guesses < 5:
#     print(f"Congratulations, you guessed {random_number}, and it took you {count} retries!")
# else:
#     print("Better luck next time.")



# from random import randint as ri

# random_number = ri(1,100)

# if random_number < 50:
#     print("The number is less than 50")
# elif random_number > 50:
#     print("The number is greater than 50")
# else:
#     print("The number is 50")

# print(random_number)

# def rect_area(len: int, wid: int) -> int: 
#     #Comments
#     return len * wid

# lenth = int(input("Enter the length:  "))
# width = int(input("Enter the width  "))

# area1 = rect_area(length, width)
# print(area1)


# def tip(total: float, percentage: float) -> float:
#     percentage_by_100 = percentage/100
#     tip_amount = total * percentage_by_100
#     return tip_amount

# print(f"The amount to tip is ${tip(100, 25)}")


# print(f"The amount to tip is ${tip(200, 50)}")


def has_more_characters(string1 : str, string2: str) -> str:
    length1 = len(string1)
    length2 = len(string2)
    if len(string1) > len(string2):
        return f"{string1} has more characters"
    elif length2 > length1:
        return f"{string2} has more characters"
    else:
        return "They are equal"
    
longer_greeting = has_more_characters([1,2,3], [1])

print(f"{longer_greeting}")
    
