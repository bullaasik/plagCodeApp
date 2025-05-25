def fibonacci_iter(var_9549):
    if not var_9549 > 1:
        return var_9549
    var_4209(var_9549)


def var_4209(var_9549):
    var_7681 = [0, 1]
    var_3903 = 2
    while var_3903 < var_9549 + 1:
        var_7681.append(var_7681[var_3903 - 1] + var_7681[var_3903 - 2])
        var_3903 += 1
    return var_7681[var_9549]


print(var_8263(10))
