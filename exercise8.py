# A function that sorts a string passed to it.

def strsort(string):
    sorted_list = sorted(string)
    return ''.join(sorted_list)


user_input = input("Type something >")

print(strsort(user_input))
