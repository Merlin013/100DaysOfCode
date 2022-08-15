def add(*args):
    print(type(args))
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(9, 10, 15, 2, 3))
