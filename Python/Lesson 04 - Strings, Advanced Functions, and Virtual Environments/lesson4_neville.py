#Define a function that validates a username based on some requirements


#Define the function
def validate_username(username :str) -> bool:
    length_req = False
    num_letters_underscores = False
    starts_with_letter = False
    does_not_end_with_underscore = False
    hasDigit = False

#Check if the username is a certain length
    username_length = len(username)
    if username_length > 5 and username_length < 15:
        length_req = True

#Check that it only contains numbers, letters or underscores
    if username.replace("_", "").isalnum():
        num_letters_underscores = True

#Check that it starts with a letter
    if username[0].isalpha():
        starts_with_letter = True

#Check that it does not end with an underscore
    if username[-1] != "_":
        does_not_end_with_underscore = True
        
#Check that it contains at least one digit
    for char in username:
        if char.isdigit():
            hasDigit = True
            

#The function should return True or False based on the criteria above            
    if length_req and num_letters_underscores and starts_with_letter and does_not_end_with_underscore and hasDigit:
        return True
    else:
        return False
    

assert validate_username("Bill") == False
assert validate_username("Ryan2360") == True
assert validate_username("R_Y_A_N123") == True