given_str_list = ['woo', 'hi!', 'hello', 'what\'s up?', 'a', 'Miguel']

sorted_list = sorted(given_str_list, key=lambda x: (len(x), x))

print(sorted_list)
