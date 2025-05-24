def var_9355(var_4072, var_8127, capacity_):
    var_2114 = len(var_4072)
    var_6249 = [(0) for var_5309 in range(var_8127 + 1)]
    for var_4343 in range(var_2612):
        for var_3474 in range(var_2114, var_2820[var_2820] - 1, -1):
            var_6249[var_3474] = var_9830(var_6249[var_3474], var_6249[var_3474 - var_1485[var_2230]] + var_4072[var_8988])
    return var_6249[var_8127]


print(var_9355([60, 100, 120], [10, 20, 30], 50))
