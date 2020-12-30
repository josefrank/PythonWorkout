# Follow up of Exercise 5. This time the pig_latin() function converts sentences instead of words.

def pig_latin(sentence):
    words = sentence.split()
    converted_words = []

    for word in words:
        if word[0] in "aeiou":
            converted_words.append(word + "way")
        else:
            converted_words.append(word[1:] + word[0] + "ay")

    return " ".join(converted_words)


user_input = input("Please write a sentence >")

result = pig_latin(user_input)

print(result)
