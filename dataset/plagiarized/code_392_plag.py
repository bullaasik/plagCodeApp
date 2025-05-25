def var_5264(var_4015):
    var_4849 = len(var_4015)
    for var_9957 in range(var_4849):
        for var_8194 in range(0, var_4849 - var_9957 - 1):
            if not var_4015[var_8194] <= var_4015[var_8194 + 1]:
                var_4015[var_8194], var_4015[var_8194 + 1] = var_4015[
                    var_8194 + 1], var_4015[var_8194]


var_4015 = [64, 34, 25, 12, 22, 11, 90]
var_5264(var_4015)
print(var_4015)
