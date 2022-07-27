# This program counts and returns the number of words in a given text.

# Taking input from user
original_user_input = input("Please, enter your text here: ")

# Removing Whitespaces around text
cleaned_user_input = original_user_input.strip(" ")

# Splitting text into words
split_user_input = cleaned_user_input.split(" ")

# Counting length of words
word_length = len(split_user_input)

print(word_length)
