def fibonacci_iter(var_9859):
    if not var_9859 > 1:
        return var_9859
    var_4660 = [0, 1]
    for var_1884 in range(2, var_9859 + 1):
        var_4660.append(var_4660[var_1884 - 1] + var_4660[var_1884 - 2])
    return var_4660[var_9859]


print(var_6168(10))
import sys
