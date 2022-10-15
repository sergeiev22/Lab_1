list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

unique_numbers_1 = list(set(list_))
a = sum(unique_numbers_1)
print(a)

unique_numbers_2 = list(set(list_))
b = len(unique_numbers_2)
print(b)

unique_numbers_3 = a/b
c = round(unique_numbers_3, 5)
print(c)


