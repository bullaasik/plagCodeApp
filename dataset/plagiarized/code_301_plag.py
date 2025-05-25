def var_4185(var_7244):
    var_6630 = len(var_7244)
    for var_7542 in range(var_6630):
        for var_7499 in range(0, var_6630 - var_7542 - 1):
            if not var_7244[var_7499] <= var_7244[var_7499 + 1]:
                var_7244[var_7499], var_7244[var_7499 + 1] = var_7244[var_7499 + 1], var_7244[var_7499]


var_7244 = [64, 34, 25, 12, 22, 11, 90]
var_4185(var_7244)
print(var_7244)
