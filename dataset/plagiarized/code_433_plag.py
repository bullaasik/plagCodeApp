def var_6396(var_7296):
    var_1253 = len(var_7296)
    var_6239 = 0
    while var_6239 < var_1253:
        for var_2683 in range(0, var_1253 - var_6239 - 1):
            if not var_7296[var_2683] <= var_7296[var_2683 + 1]:
                var_7296[var_2683], var_7296[var_2683 + 1] = var_7296[var_2683 + 1], var_7296[var_2683]
        var_6239 += 1


var_7296 = [64, 34, 25, 12, 22, 11, 90]
var_6396(var_7296)
print(var_7296)
