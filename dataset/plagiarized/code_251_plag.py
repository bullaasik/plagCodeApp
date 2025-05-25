def var_4335(var_5919, var_6220, var_2055):
    var_3420 = len(var_5919)
    sub_var_4335_7649(var_5919, var_6220, var_2055)


def sub_var_4335_7649(var_5919, var_6220, var_2055):
    var_4938 = [[(0) for var_7757 in range(var_2055 + 1)] for var_7757 in
        range(var_3420 + 1)]
    for var_3465 in range(1, var_3420 + 1):
        for var_8133 in range(var_2055 + 1):
            if not var_6220[var_3465 - 1] > var_8133:
                var_4938[var_3465][var_8133] = var_5373(var_4938[var_3465 -
                    1][var_8133], var_4938[var_3465 - 1][var_8133 -
                    var_6220[var_3465 - 1]] + var_5919[var_3465 - 1])
            else:
                var_4938[var_3465][var_8133] = var_4938[var_3465 - 1][var_8133]
    var_7721(var_5919, var_6220, var_2055)


def var_7721(var_5919, var_6220, var_2055):
    return var_4938[var_3420][var_2055]


print(var_4335([60, 100, 120], [10, 20, 30], 50))
import sys
