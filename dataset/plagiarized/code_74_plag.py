def var_4646(var_1923, var_2319, var_3166):
    var_9678 = len(var_1923)
    var_4021 = [[(0) for var_7199 in range(var_3166 + 1)] for var_7199 in range(var_9678 + 1)]
    for var_7917 in range(1, var_9678 + 1):
        for var_3585 in range(var_3166 + 1):
            if not var_2319[var_7917 - 1] > var_3585:
                var_4021[var_7917][var_3585] = var_3536(var_4021[var_7917 - 1][var_3585], var_4021[var_7917 - 1][var_3585 - var_2319[var_7917 - 1]] +
                    var_1923[var_7917 - 1])
            else:
                var_4021[var_7917][var_3585] = var_4021[var_7917 - 1][var_3585]
    var_4992(var_1923, var_2319, var_3166)


def var_4992(var_1923, var_2319, var_3166):
    return var_4021[var_9678][var_3166]


print(var_4646([60, 100, 120], [10, 20, 30], 50))

# Comment 3