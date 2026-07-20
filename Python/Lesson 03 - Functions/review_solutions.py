#Problem 1 - Temperature Advisor

# temp = float(input("Enter the temperature outside:  "))
# raining = input("Is it raining ('yes'/'no'):  ")

# if temp < 40:
#     output = "Bring a coat. "
# elif temp <= 60: 
#     output = "Bring a jacket. "
# else:
#     output = "Enjoy the weather! "

# if raining == "yes":
#     output = f"{output}" + "Bring an umbrella"

# print(output)


#Problem 2 - Fizzbuzz with a Twist

# start = int(input("Enter the start value:  "))
# stop = int(input("Enter the stop value:  "))

# def fizzBuzz(beginning: int, end: int) -> int:
#     counter = 0
#     for number in range(beginning,end+1):
#         if number % 3 == 0 and number % 5 ==0:
#             print("FizzBuzz")
#             counter += 1
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
#     return counter

# amount = fizzBuzz(start, stop)

# print(f"There are {amount} of fizzBuzzes in between and including {start} and {stop}.")


#Problem 3 - Password checker

# digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# #digit_list = [str(i) for i in range (10)]
# def password_checker(password: str) -> str:
#     hasDigit = False
#     hasUpperCase = False
#     password_len = len(password)
#     if password_len < 8:
#         #If password is less than 8 characters...
#         return "Weak"
#     else:
#         #If password is greater than or equal to 8 characters...
#         for letter in password:
#             #Check if the letter is equal to a digit
#             for digit in digit_list:
#                 if letter == digit:
#                     #If one of the letters is equal to a digit...
#                     hasDigit = True
#                     break
            
#             if letter not in digit_list and letter == letter.upper():
#                 print(letter)
#                 hasUpperCase = True


#         if hasDigit and hasUpperCase:
#             return "Strong"
#         else:
#             return "Medium"


# user_password = input("Enter a password (Make it strong!):  ")
# password_strength = password_checker(user_password)

# while password_strength != "Strong":
#     print(f"The password strength is {password_strength}")
#     user_password = input("Enter a password (Make it strong!):  ")
#     password_strength = password_checker(user_password)

# print(f"This password is {password_strength}, great job!")

#Problem 4 - Grade Calculator
def letter_grade(score: float) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

try:
    students = int(input("How many grades are there to enter?  "))
    total_scores = 0
    for student in range(1, students+1):
        score = float(input(f"Enter student #{student}'s score:  "))
        total_scores += score
        print(f"Student #{student} got a letter grade {letter_grade(score)}")


    print(f"The class average was {total_scores/students}, this is a {letter_grade(total_scores/students)}")
except ZeroDivisionError as e:
    print("There were no students")
    