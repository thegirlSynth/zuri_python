# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

def read_file_content(filename):
    with open(filename) as file:
        content = file.read()
        
    return content


def count_words():
    text = read_file_content("./story.txt")
    
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = {}
    split_text = cleaned_text.split()

    for word in split_text:
        words[word] = split_text.count(word)
        
    
    return words


print(count_words())

