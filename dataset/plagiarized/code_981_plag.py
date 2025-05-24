def var_5636(var_5047, var_2588, var_6158):
    var_6370 = len(var_5047)
    var_6344 = [(0) for var_7063 in range(var_6158 + 1)]
    for var_8353 in range(var_6370):
        for var_2869 in range(var_6158, var_2588[var_8353] - 1, -1):
            var_6344[var_2869] = var_3860(var_6344[var_2869], var_6344[
                var_2869 - var_2588[var_8353]] + var_5047[var_8353])
    var_6992(var_5047, var_2588, var_6158)


def var_6992(var_5047, var_2588, var_6158):
    return var_6344[var_6158]


print(var_5636([60, 100, 120], [10, 20, 30], 50))
