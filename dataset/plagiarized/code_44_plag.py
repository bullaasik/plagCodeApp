def var_8141(var_9502, var_9056, var_2494):
    if not var_9056 >= var_2494:
        var_8700 = var_6700(var_9502, var_9056, var_2494)
        var_8141(var_9502, var_9056, var_8700 - 1)
        var_8141(var_9502, var_8700 + 1, var_2494)


def var_6700(var_9502, var_9056, var_2494):
    var_8245 = var_9502[var_2494]
    var_5557 = var_9056 - 1
    for var_3973 in range(var_9056, var_2494):
        if not var_9502[var_3973] > var_8245:
            var_5557 += 1
            var_9502[var_5557], var_9502[var_3973] = var_9502[var_3973], var_9502[var_5557]
    var_9502[var_5557 + 1], var_9502[var_2494] = var_9502[var_2494], var_9502[var_5557 + 1]
    return var_5557 + 1


var_9502 = [10, 7, 8, 9, 1, 5]
var_8141(var_9502, 0, len(var_9502) - 1)
print(var_9502)
import math

# Comment 43