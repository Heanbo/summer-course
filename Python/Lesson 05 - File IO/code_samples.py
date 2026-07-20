#open a file and print each line in it to the terminal
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

#write this to file
text_to_write = [
    "This is a new line of text.\n",
    "Here is another line.\n",
    "And yet another line.\n"
]
#this syntax handles the file opening and closing automatically
with open('output.txt', 'w') as file:
    for text in text_to_write:
        file.write(text)

#read the contents of a file and store it in the variable 'content'
file_handle = open('output.txt', 'r')
content = file_handle.read()
#you have to manually close it when using this syntax
file_handle.close()

#this syntax handles the file opening and closing automatically
#so you can just focus on assigning the contents to a variable
with open('output.txt', 'r') as file_handle:
    content = file_handle.read()

# Open 'input.txt' in read mode and 'output.txt' in write mode using context managers
# This ensures files are properly closed after operations
with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
# Iterate through each line in the input file
    for line in input:
        # Strip whitespace from the beginning and end of the line,
        # convert it to uppercase, add a newline character,
        # and write it to the output file
        output.write(line.strip().upper() + '\n')

