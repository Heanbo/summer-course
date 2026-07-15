### has more characters function


def has_more_characters(str1: str, str2: str) -> str:
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else:
        return "Equal length"
    
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print(has_more_characters(string1, string2))