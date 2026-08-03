# Write a program that accepts a simple mathematical expression as input, 
# evaluates the expression, and displays the resulting solution to the user. 


expression = input("Enter a simple expression (e.g. 5 + 9): ")

# Split the expression into parts
parts = expression.split()

num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Unsupported operator")
    exit()

print("Result:", result)