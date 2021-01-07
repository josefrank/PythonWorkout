"""
The bottom line of this exercise is the idea creating a function able to
retrieve data from a sequence (list, tuple, string) and return a another sequence of
the same type. This is possible thanks to the idea of slicing [a:b] and wouldn't be
possible just accessing the elements via index [a].
"""


def first_last(sequence):
    return sequence[:1] + sequence[-1:]


numbers = (2, 5, 6, 8, 1)

result = first_last(numbers)

print(result)
print(type(result))
