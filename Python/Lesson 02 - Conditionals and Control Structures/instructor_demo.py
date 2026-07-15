# #In Class Exercise 1 (Postive, Negative, or Zero)

# user_num = float(input("Enter a number:  "))

# if user_num > 0:
#     print("Positive")
# elif user_num < 0:
#     print("Negative")
# else:
#     print("The number is 0")

# #Comment
# user_num = float(input("Enter a number:  "))

# if user_num > 0:
#     print("Positive")
# elif user_num < 0:
#     print("Negative")
# else:
#     print("The number is 0")

# user_num = float(input("Enter a number:  "))

# if user_num > 0:
#     print("Positive")
# elif user_num < 0:
#     print("Negative")
# else:
#     print("The number is 0")



# user_number = int(input("Enter an even integer number:  "))
# while user_number % 2 == 1:
#     user_number = int(input("Enter an even integer number:  "))

# print(f"Good job!  You entered an even number, {user_number}")


secret_number = 22

user_guess = int(input("Guess an integer number:  "))
count = 1

while user_guess != secret_number and count < 5:
    if user_guess < secret_number:
        print("Your guess was too low!")

    else:
        print("Your guess was too high!")

    user_guess = int(input("Guess an integer number:  "))
    count += 1

if user_guess == secret_number:
    print(f"Congratulations, you guessed the correct number, {user_guess}")
    print(f"It took you {count} guesses.")
else:
    print(f"Guess better next time!")



