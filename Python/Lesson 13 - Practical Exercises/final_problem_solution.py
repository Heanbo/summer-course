#Copy your favorite song lyrics into a string variable.  Determine all of the unique words in the song and the number of times they occur.
# five different solutions shown below

#######################  SOLUTION 1 ##########################################
# # define a function to do the work for us
def count_words(input_str: str) -> dict[str, int]:
    cleaned_list = input_str.replace(",", "").lower().split()
    result = {}
    for word in cleaned_list:
        if word not in result:
            result[word] = 1
        else:
            result[word] = result[word] + 1
    return result


# call the function below
input_str = "mary had a little lamb, little lamb, little lamb"
word_counts = count_words(input_str)
print(word_counts)

####################### SOLUTION 2 ############################################
def count_words_two(input_str: str) -> dict[str, int]:
    cleaned_list = input_str.replace(",", "").lower().split()

    unique_words = set(cleaned_list)
    word_counts = {}

    for word in unique_words:
        word_counts[word] = cleaned_list.count(word)

    return word_counts


word_counts = count_words_two(input_str)
print(word_counts)

####################### SOLUTION 3 ############################################

def count_words_four(input_str: str) -> tuple[list[str], list[int]]:
    cleaned_list = input_str.replace(",", "").lower().split()
    words = []
    counts = []

    for word in cleaned_list:
        if word not in words:
            words.append(word)
            counts.append(1)
        else:
            counts[words.index(word)] = counts[words.index(word)] + 1
    return words, counts


word_counts = count_words_four(input_str)
print(word_counts)

####################### SOLUTION 4 ############################################
from collections import Counter


def count_words_three(input_str: str) -> dict[str, int]:
    cleaned_list = input_str.replace(",", "").lower().split()
    return dict(Counter(cleaned_list))

word_counts = count_words_three(input_str)
print(word_counts)


####################### SOLUTION 5 ############################################
def count_words_five(input_str):
    cleaned_list = input_str.replace(",", "").lower().split()

    unique_words = set(cleaned_list)
    result = {}

    # initialize dict
    for word in unique_words:
        result[word] = 0

    for word in cleaned_list:
        result[word] += 1
    
    return result

word_counts = count_words_five(input_str)
print(word_counts)
