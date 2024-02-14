given_num_list = [5, 1, 6, 3, 8, -2, -3]
given_n = 3

result = list(map(lambda x: x ** given_n, given_num_list))

print(f"Given list: {given_num_list}\nEach number was raised to the following power: {given_n}\nResult: {result}")
