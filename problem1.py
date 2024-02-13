'''
Objective: Write a program that uses a lambda function to compute the sum of the digits of a given number.
Hint: You may need to convert the number to a str to iterate over its digits, then back to ints to sum them.
'''

from functools import reduce


numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)
