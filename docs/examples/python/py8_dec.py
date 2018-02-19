def off_by_one(original_function):
    def new_function(x, y):
        return original_function(x, y) + 1

    return new_function


def multiply_by_two(f):
    def new_f(x, y):
        return f(x, y) * 2

    return new_f


@off_by_one
def add(x, y):
    return x + y


@multiply_by_two
def add2(x, y):
    return x + y


@off_by_one
@multiply_by_two
def add3(x, y):
    return x+y


print(add(2, 2))
print(add2(2, 2))
print(add3(2, 2))
