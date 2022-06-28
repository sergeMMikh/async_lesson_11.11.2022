def range(start, end):

    while start < end:
        yield start
        start += 1

my_range = range(1, 10)

print(my_range)
for item in my_range:
    print(item)
