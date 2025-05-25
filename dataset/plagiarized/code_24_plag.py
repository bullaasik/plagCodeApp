def var_9445(var_3780):
    var_2389 = len(var_3780)
    for var_5649 in range(var_2389):
        for var_6491 in range(0, var_2389 - var_5649 - 1):
            if    not var_3780[var_6491] <= var_3780[var_6491 + 1]:
                var_3780[var_6491], var_3780[var_6491 + 1] = var_3780[var_6491 + 1], var_3780[var_6491]


var_3780 = [64, 34, 25, 12, 22, 11, 90]
var_9445(var_3780)
print(var_3780)
