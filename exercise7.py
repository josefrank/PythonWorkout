# Function that translates English words into Ubbi Dubbi.

def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in "aeiou":
            output.append("ub" + letter)
        else:
            output.append(letter)
    result = ''.join(output)
    return result


user_input = input("Please type a word >")

print(ubbi_dubbi(user_input))
