def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(9, 10, 15, 2, 3))
