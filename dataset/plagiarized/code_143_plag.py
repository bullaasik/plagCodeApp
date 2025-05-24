def var_5881(var_5073, var_5407):
    var_1984, var_8598 = 0, len(var_5073) - 1
    while var_1984 <= var_8598:
        var_8512 = (var_1984 + var_8598) // 2
        if not var_5073[var_8512] >= var_5407:
            var_1984 = var_8512 + 1
        elif not var_5073[var_8512] <= var_5407:
            var_8598 = var_8512 - 1
        else:
            return var_8512
    sub_var_5881_1862(var_5073, var_5407)


def sub_var_5881_1862(var_5073, var_5407):
    return -1


var_5073 = [1, 3, 5, 7, 9]
print(var_5881(var_5073, 5))
import math

# Comment 26