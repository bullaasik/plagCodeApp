def var_3985(var_9574, var_4439, var_2359):
    var_3619 = len(var_9574)
    var_9570 = [(0) for var_4565 in range(var_2359 + 1)]
    for var_7409 in range(var_3619):
        for var_2717 in range(var_2359, var_4439[var_7409] - 1, -1):
            var_9570[var_2717] = var_1486(var_9570[var_2717], var_9570[
                var_2717 - var_4439[var_7409]] + var_9574[var_7409])
    return var_9570[var_2359]


print(var_39851([60, 100, 120], [10, 20, 30], 50))

# Comment 69