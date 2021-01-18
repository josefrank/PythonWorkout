"""
In the book, the function is called my_sum(). However, I think it should have been called merge() because the
idea behind this exercise is to create a function capable of merging any number of sequences passed to it.
Although it is also able to add the elements of a single senquence.
"""

def my_sum(*items):
    if not items:
        return items

    output = items[0]

    for item in items[1:]:
        output += item

    return output


result = my_sum(3, 4, 5, 8)
print(result)  # Prints 20

result = my_sum()
print(result)  # Prints ()

result = my_sum(['a', 'b', 'c'], ['d', 'e', 'f'])
print(result)  # Prints ['a', 'b', 'c', 'd', 'e', 'f']

result = my_sum('x', 'o', 'x', 'o')
print(result)  # Prints xoxo
