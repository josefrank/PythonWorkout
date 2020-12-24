# Write a sum() like function.


def mySum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


myList = [3, 5, 6, 6, 1]

result = mySum(*myList)
print(result)
