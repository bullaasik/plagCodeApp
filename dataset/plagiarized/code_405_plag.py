def var_2786(var_3789):
    var_7708 = len(var_3789)
    for var_9265 in range(var_7708):
        for var_7625 in range(0, var_7708 - var_9265 - 1):
            if not var_3789[var_7625] <= var_3789[var_7625 + 1]:
                var_3789[var_7625], var_3789[var_7625 + 1] = var_3789[
                    var_7625 + 1], var_3789[var_7625]


var_3789 = [64, 34, 25, 12, 22, 11, 90]
var_2786(var_3789)
print(var_3789)
