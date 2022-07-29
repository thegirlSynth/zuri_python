# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # for each letter in the words in the first string, count how many times it has occurred
    # Check for the same letter with the same count in second string
    # if they are equal, return True.
    # else, return False

    word = word.islower()
    anagram = anagram.islower()

    new_word = word.replace(" ", "")
    word_letters = {}
    for letter in new_word:
        word_letters[letter] = new_word.count(letter)

    new_anagram = anagram.replace(" ", "")
    anagram_letters = {}
    for letter in new_anagram:
        anagram_letters[letter] = new_anagram.count(letter)


    shared_keys = set(word_letters.keys()) & set(anagram_letters.keys())

    if not ( len(shared_keys) == len(word_letters.keys()) and len(shared_keys) == len(anagram_letters.keys())):
        return False

    if word_letters == anagram_letters:
        return True

    return False

    


    print(word_letters)  
    print(anagram_letters)
    
    return True


#Check
Return = find_anagram("Dormitory", "Dirty room")
print(Return)
Return = find_anagram("hello", "ellho")
print(Return)
Return = find_anagram("heavy rain", "hire a navy")
print(Return)

