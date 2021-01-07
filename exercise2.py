"""
A sum() like function with the feature of taking more than a sequence.

Note: The splat operator [as in mySum(*numbers)] always returns a tuple. If attempting
to past a sequence (list, tuple, string) as an argument in the function call of MySum()
will result in a type error because the *numbers parameter will convert the sequence
into a tuple whose first element would be the sequence itself that wound not be possible
to be added to the total variable because it is an integer.

The solution to this problem is to add the splat (*) operator in the function call too, which
results in the argument passed to be "unpacked" as it would have been individual values.
"""


def mySum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


myList = [3, 5, 6, 6, 1]

result = mySum(*myList)
print(result)

result = mySum(3, 5, 6, 6, 1)
print(result)
