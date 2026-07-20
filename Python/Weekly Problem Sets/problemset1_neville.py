import math

#Problem - Personalized Card

# #Get the users name
# user_name = input("Enter your name:  ")
# #Get their favorite number
# user_number = int(input("Enter your favorite integer number:  "))


# #Define a function that creates a personalized card based on the user's input
# def personalized_card(symbol: str, name: str, favorite_number: int) -> None:
#     #Inside of the function, create both sentences
#     name_sentence = "Hello, " + name
#     number_sentence = "Your favorite number is " + str(favorite_number)

#     #Take the length of both, and compare them.  The longest sentence is going to drive the size of the card.

#     sentence_1_len = len(name_sentence)
#     sentence_2_len = len(number_sentence)

#     sentence_len_diff = abs(sentence_2_len - sentence_1_len)
#     if sentence_1_len >= sentence_2_len:
#         max_len = sentence_1_len
#     else:
#         max_len = sentence_2_len
    

# #Create the card based on that.
# #Print out the card based on which sentence is longer
#     if sentence_2_len >= sentence_1_len:
#         print(symbol * (max_len + 6))
#         print(symbol + "  " + name_sentence + " " * sentence_len_diff + "  " + symbol)
#         print(symbol + "  " + number_sentence + "  " + symbol)
#         print(symbol * (max_len + 6))
#     else:
#         print(symbol * (max_len + 6))
#         print(symbol + "  " + name_sentence + "  " + symbol)
#         print(symbol + "  " + number_sentence + " " * sentence_len_diff + "  " + symbol)
#         print(symbol * (max_len + 6))

# #Call a function that creates the personalized card

# personalized_card('$', user_name, user_number)



#It's about the problem solving process

#1) Write Inputs, Outputs, and do your best to fill in the middle.  Do this with comments, not code.
#2) Do the smallest amount of work, and test it, rinse and repeat.  Translate your comments into code.
#3) Build intelligent test cases, and test thoroughly.  Ask yourself why things are happening.



# #Problem 2 - Sequence Explorer

# for i in range(1, 16):
#     print(i, end=" ")

# print()

# for j in range(2, 31, 2):
#         print(j, end=" ")

# print()

# for k in range(20, -1, -2):
#         print(k, end=" ")

# print()

# def print_range(start: int, stop: int, step: int) -> None:
#     for number in range(start, stop, step):
#         print(number, end=" ")

# print_range(20, -1, -2)

# print()
# print(1,2,3,4)


# range_3 = range(0, 21, 2)[::-1]
# range_3 = range(21, -1, -2)

# # print(*range_3) -> range(21, -1, -2) -> 21 19 17...

# name_list = ["Robert", "Miguel", "Ben"]

# print(*name_list)


#Problem 4 - Fuel Efficiency Calculator

distance = float(input("Enter the distance in miles:  "))
fuel_efficiency = float(input("Enter the vehicle's fuel efficiency in MPG:  "))
fuel_cost = float(input("Enter the outrageous gas price:  "))

gallons_needed = round(distance/fuel_efficiency,2)
total_fuel_cost = gallons_needed * fuel_cost

print("\n\n")

print("--- Road Trip Fuel Estimate ---")
print(f"Distance:\t {distance} Miles")
print(f"Fuel efficiency: {fuel_efficiency} MPG")
print(f"Gas Price:\t {fuel_cost} / Gallon")
print()
print(f"Gallons Needed:\t {gallons_needed} Gallons")
print(f"Total Fuel Cost: ${total_fuel_cost:.2f}")