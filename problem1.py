from functools import reduce


given_num = 12345678

sum_of_digits = reduce(lambda x, y: int(x) + int(y), str(given_num))

print(f"Number given: {given_num}\nSum of its digits: {sum_of_digits}")
