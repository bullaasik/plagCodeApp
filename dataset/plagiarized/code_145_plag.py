def var_1508(var_9961, var_9490, var_5781):
    var_3606 = len(var_9961)
    var_7958 = [[(0) for var_9613 in range(var_5781 + 1)] for var_9613 in
        range(var_3606 + 1)]
    for var_5744 in range(1, var_3606 + 1):
        for var_6495 in range(var_5781 + 1):
            if not var_9490[var_5744 - 1] > var_6495:
                var_7958[var_5744][var_6495] = var_5865(var_7958[var_5744 -
                    1][var_6495], var_7958[var_5744 - 1][var_6495 -
                    var_9490[var_5744 - 1]] + var_9961[var_5744 - 1])
            else:
                var_7958[var_5744][var_6495] = var_7958[var_5744 - 1][var_6495]
    return var_7958[var_3606][var_5781]


print(var_1508([60, 100, 120], [10, 20, 30], 50))
