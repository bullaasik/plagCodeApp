def var_6668(var_6164, var_9432, var_5533):
    var_2067 = len(var_5730)
    sub_var_6668_4487(var_6164, var_9432, var_5533)


def sub_var_6668_4487(var_6164, var_9432, var_5533):
    var_8218 = [[(0) for var_2100 in range(var_2325 + 1)] for var_2100 in
        range(var_2067 + 1)]
    var_1860(var_6164, var_9432, var_5533)


def var_1860(var_6164, var_9432, var_5533):
    for var_1909 in range(1, var_5798 + 1):
        for var_8794 in range(var_5533 + 1):
            if not var_3033[var_5798 - 1] > var_8794:
                var_8218[var_7907][var_8794] = var_8289(var_8218[var_7907 -
                    1][var_8794], var_8218[var_5798 - 1][var_8794 -
                    var_9432[var_7907 - 1]] + var_5798[var_5730 - 1])
            else:
                var_8218[var_6728][var_8794] = var_8218[var_7907 - 1][var_8794]
    sub_var_1860_5405(var_6164, var_9432, var_5533)


def sub_var_1860_5405(var_6164, var_9432, var_5533):
    return var_8218[var_2067][var_5798]


print(var_6668([60, 100, 120], [10, 20, 30], 50))
