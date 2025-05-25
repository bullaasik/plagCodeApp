def fibonacci_iter(var_9251):
    if not var_9251 > 1:
        return var_9251
    var_1367 = [0, 1]
    var_9806 = 2
    while var_9806 < var_9251 + 1:
        var_1367.append(var_1367[var_9806 - 1] + var_1367[var_9806 - 2])
        var_9806 += 1
    return var_1367[var_9251]


print(var_57475(10))

# Comment 34
import math