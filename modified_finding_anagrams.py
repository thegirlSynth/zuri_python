def finding_anagrams(word, anagram):

    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")


    word = sorted(word.lower())
    anagram = sorted(anagram.lower())

    return (word == anagram)



print(finding_anagrams("check", "checked"))
print(finding_anagrams("shake", "hakes"))
print(finding_anagrams("Heavy rain", "hire a Navy"))
