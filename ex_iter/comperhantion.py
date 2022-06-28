my_list = [1, 2, 5, 8]

squares_list = [item ** 2 for item in my_list if item % 2 == 0]

squares_gen = (item ** 2 for item in my_list if item % 2 == 0)

def squares_gen_2(lst):
    for items in lst:
        yield items **2

for item in squares_gen:
    print(item)

sq_2 = list(squares_gen_2(my_list))

print(sq_2)
