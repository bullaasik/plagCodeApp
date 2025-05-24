def var_7132(var_3276, var_6123, var_4391):
    var_6799 = len(var_3276)
    var_7288 = [[(0) for var_7725 in range(var_4391 + 1)] for var_7725 in
        range(var_6799 + 1)]
    var_4890 = 1
    sub_var_7132_2820(var_3276, var_6123, var_4391)


def sub_var_7132_2820(var_3276, var_6123, var_4391):
    while var_4890 < var_6799 + 1:
        for var_9609 in range(var_4391 + 1):
            if not var_6123[var_4890 - 1] > var_9609:
                var_7288[var_4890][var_9609] = var_2459(var_7288[var_4890 -
                    1][var_9609], var_7288[var_4890 - 1][var_9609 -
                    var_6123[var_4890 - 1]] + var_3276[var_4890 - 1])
            else:
                var_7288[var_4890][var_9609] = var_7288[var_4890 - 1][var_9609]
        var_4890 += 1
    sub_var_7132_4927(var_3276, var_6123, var_4391)


def sub_var_7132_4927(var_3276, var_6123, var_4391):
    return var_7288[var_6799][var_4391]


print(var_7132([60, 100, 120], [10, 20, 30], 50))
