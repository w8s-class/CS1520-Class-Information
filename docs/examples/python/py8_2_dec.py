import timeit


def time(original_function):
    def new_function(*args, **kwargs):
        start = timeit.default_timer()
        original_function(*args, **kwargs)
        stop = timeit.default_timer()
        print(start - stop)
    return new_function


@time
def loopity_loop(length):
    newArr = []
    for x in range(length):
        newArr.append(x * 2)


@time
def loopity_loop_comp(length):
    newArr = [x*2 for x in range(length)]


print(loopity_loop(10000))
print(loopity_loop_comp(10000))
