def find_max(num_list, lambda_func):
    curr_max = num_list[0]

    for num in num_list:
        curr_max = lambda_func(curr_max, num)
    
    return curr_max

determine_max = lambda x, y: x if x > y else y
given_num_list = [78, 40, 81, 3, 9, 11, -1, 0, -3, 101, 99]

print(f"Numbers: {given_num_list}\nMax: {find_max(given_num_list, determine_max)}")
