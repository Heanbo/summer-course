# read test.txt find min, max, and average value of 100 rand int, do not use min() or max() functions
total = 0
number_of_lines = 0
min_value = None
max_value = None
with open('test.txt','r') as file:
    lines = file.readlines()
    for lines in lines:
        #DEBUG LINES
        #print(int(lines))
        number_of_lines += 1
        total = total + int(lines)
        if min_value is None or int(lines) < min_value:
            min_value = int(lines)
        if max_value is None or int(lines) > max_value:
            max_value = int(lines)
 
print(f"Total: {total}")
print(f"Count: {number_of_lines}")
print(f"Min: {min_value}, Max: {max_value}")
print(f"Average: {total / number_of_lines}")