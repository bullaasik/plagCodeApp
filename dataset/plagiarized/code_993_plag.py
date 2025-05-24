def var_7002(var_6562, var_1729, var_9664):
    var_6032 = len(var_6562)
    sub_var_7002_9585(var_6562, var_1729, var_9664)


def sub_var_7002_9585(var_6562, var_1729, var_9664):
    var_5226(var_6562, var_1729, var_9664)


def var_5226(var_6562, var_1729, var_9664):
    var_1667 = [(0) for var_9544 in range(var_9664 + 1)]
    for var_3482 in range(var_6032):
        for var_6477 in range(var_9664, var_1729[var_3482] - 1, -1):
            var_1667[var_6477] = var_3976(var_1667[var_6477], var_1667[
                var_6477 - var_1729[var_3482]] + var_6562[var_3482])
    sub_var_5226_8484(var_6562, var_1729, var_9664)


def sub_var_5226_8484(var_6562, var_1729, var_9664):
    return var_1667[var_9664]


print(var_7002([60, 100, 120], [10, 20, 30], 50))
import os

# Comment 62