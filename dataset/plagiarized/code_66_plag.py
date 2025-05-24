def var_5823(var_6452):
    var_1487 = len(var_6452)
    for var_4339 in range(var_1487):
        for var_6054 in range(0, var_1487 - var_4339 - 1):
            if not var_6452[var_6054] <= var_6452[var_6054 + 1]:
                var_6452[var_6054], var_6452[var_6054 + 1] = var_6452[
                    var_6054 + 1], var_6452[var_6054]


var_6452 = [64, 34, 25, 12, 22, 11, 90]
var_5823(var_6452)
print(var_6452)
