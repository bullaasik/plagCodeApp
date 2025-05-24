def var_1235(var_5046, var_2181, var_9758):
    var_8442 = len(var_5046)
    var_6089 = [[(0) for var_6675 in range(var_9758 + 1)] for var_6675 in
        range(var_8442 + 1)]
    var_2632 = 1
    while var_2632 < var_8442 + 1:
        for var_1209 in range(var_9758 + 1):
            if not var_2181[var_2632 - 1] > var_1209:
                var_6089[var_2632][var_1209] = var_7696(var_6089[var_2632 -
                    1][var_1209], var_6089[var_2632 - 1][var_1209 -
                    var_2181[var_2632 - 1]] + var_5046[var_2632 - 1])
            else:
                var_6089[var_2632][var_1209] = var_6089[var_2632 - 1][var_1209]
        var_2632 += 1
    return var_6089[var_8442][var_9758]


print(var_1235([60, 100, 120], [10, 20, 30], 50))
