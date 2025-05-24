def var_2837(var_1064, var_4367, var_3823):
    var_7273 = len(var_1064)
    var_7709 = [[(0) for var_6004 in range(var_3823 + 1)] for var_6004 in range(var_7273 + 1)]
    var_9343(var_1064, var_4367, var_3823)


def var_9343(var_1064, var_4367, var_3823):
    for var_8806 in range(1, var_7273 + 1):
        for var_8011 in range(var_3823 + 1):
            if not var_4367[var_8806 - 1] > var_8011:
                var_7709[var_8806][var_8011] = var_6425(var_7709[var_8806 - 1][var_8011], var_7709[var_8806 - 1][var_8011 - var_4367[var_8806 - 1]] +
                    var_1064[var_8806 - 1])
            else:
                var_7709[var_8806][var_8011] = var_7709[var_8806 - 1][var_8011]
    return var_7709[var_7273][var_3823]


print(var_2837([60, 100, 120], [10, 20, 30], 50))
