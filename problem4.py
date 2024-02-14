given_list1 = [1, 2, 3, 4, 5]
given_list2 = [4, 5, 6, 7, 8]

intersection = list(filter(lambda x: x in given_list1, given_list2))

print(f"List 1:{given_list1}\nList 2:{given_list2}\nIntersection: {intersection}")
