# ### RECURSION NOTES ####

### PALIDROME CHECKER ###

# def palindrome(input_str):
#     if input_str == "":
#     ## IF THERE ARE NO LETTERS TO COMPARE, EXIT ##
#         return True
#     if len(input_str) == 1:
#     ## IF THERE IS ONLY ONE LETTER TO COMPARE TO, EXIT ##
#         return True

#     if input_str[0] != input_str[-1]: 
#     ## IF THE FIRST LETTER IS NOT THE SAME AS THE LAST, EXIT ##
#         return False

#     print(f"Computing string")
#     result = palindrome(input_str[1:-1])
#     return result

# word = input("enter word")
# palindrome(word)
# print(result)


### LIST SUM CALCULATOR ###

# def sum_of_list(list):
#     if len(list) == 0:
#         return 0
#     if len(list) == 1:
#         return list[0]
#     return list[0] + sum_of_list(list[1:])

# mylist = [10,30,20,4,5,6,7]
# result = sum_of_list(mylist)
# print(result)


### FIBINOCI CALCULATION ###

# def fib(n:int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(6))


    
    