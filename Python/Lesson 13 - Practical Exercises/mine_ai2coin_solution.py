# Write a program that calculates however many semiprime 
# numbers the user specifies and prints them to the screen.


# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Check if a number is semiprime
def is_semiprime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            if is_prime(i) and is_prime(n // i):
                return True
        i += 1
    return False

# Main program
count = int(input("How many semiprime numbers should be displayed? "))

found = 0
num = 4  # First semiprime

while found < count:
    if is_semiprime(num):
        print(num, end=' ')
        found += 1
    num += 1