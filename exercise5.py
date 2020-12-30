# A function that translates words into Pig Latin.

def pig_latin():
    word = input("Please type a word >")
    vowels = "aeiou"
    is_vowel = word[0] in vowels
    if is_vowel:
        print(word + "way")
    else:
        print(word[1:] + word[0] + "ay")


pig_latin()
