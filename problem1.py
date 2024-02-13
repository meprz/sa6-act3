from functools import reduce


given_num = 12345
copy_given_num = given_num
digits = []

while copy_given_num > 0:
    digits.append(copy_given_num % 10)
    copy_given_num //= 10

result = reduce(lambda x, y: x + y, digits)
print(result)
