import timeit


def time(original_function):
    def new_function(*args, **kwargs):
        start = timeit.default_timer()
        res = original_function(*args, **kwargs)
        stop = timeit.default_timer()
        print(start - stop)
        return res
    return new_function


@time
def loopity_loop(length):
    new_arr = []
    for x in range(length):
        new_arr.append(x * 2)

    return sum(new_arr)


@time
def loopity_loop_comp(length, multiplier):
    new_arr = [x*multiplier for x in range(length)]
    return sum(new_arr)


print('For %d' % loopity_loop(100000))
print('Comp %d' % loopity_loop_comp(100000, 3))
