def var_4992(var_6104):
    var_5493 = len(var_6104)
    for var_5339 in range(var_5493):
        for var_6126 in range(0, var_5493 - var_5339 - 1):
            if not var_6104[var_6126] <= var_6104[var_6126 + 1]:
                var_6104[var_6126], var_6104[var_6126 + 1] = var_6104[
                    var_6126 + 1], var_6104[var_6126]


var_6104 = [64, 34, 25, 12, 22, 11, 90]
var_4992(var_6104)
print(var_6104)
