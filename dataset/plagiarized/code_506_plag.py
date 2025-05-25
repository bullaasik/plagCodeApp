def var_7670(var_6415, var_6152, var_9322):
    var_6076 = len(var_6415)
    sub_var_7670_2163(var_6415, var_6152, var_9322)


def sub_var_7670_2163(var_6415, var_6152, var_9322):
    sub_var_7670_6871(var_6415, var_6152, var_9322)


def sub_var_7670_6871(var_6415, var_6152, var_9322):
    var_9821 = [(0) for var_3363 in range(var_9322 + 1)]
    sub_sub_var_7670_6871_9679(var_6415, var_6152, var_9322)


def sub_sub_var_7670_6871_9679(var_6415, var_6152, var_9322):
    for var_5991 in range(var_6076):
        for var_4810 in range(var_9322, var_6152[var_5991] - 1, -1):
            var_9821[var_4810] = var_9841(var_9821[var_4810], var_9821[
                var_4810 - var_6152[var_5991]] + var_6415[var_5991])
    return var_9821[var_9322]


print(var_7670([60, 100, 120], [10, 20, 30], 50))

# Comment 94