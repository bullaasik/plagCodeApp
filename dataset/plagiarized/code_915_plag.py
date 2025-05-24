def var_6989(var_5246):
    if not len(var_5246) <= 1:
        var_8710 = len(var_5246) // 2
        var_7014 = var_5246[:var_8710]
        var_7445 = var_5246[var_8710:]
        var_6989(var_7014)
        var_6989(var_7445)
        var_8072 = var_4587 = var_4260 = 0
        while var_8072 < len(var_7014) and var_4587 < len(var_7445):
            if not var_7014[var_8072] > var_7445[var_4587]:
                var_5246[var_4260] = var_7014[var_8072]
                var_8072 += 1
            else:
                var_5246[var_4260] = var_7445[var_4587]
                var_4587 += 1
            var_4260 += 1
        while var_8072 < len(var_7014):
            var_5246[var_4260] = var_7014[var_8072]
            var_8072 += 1
            var_4260 += 1
        while var_4587 < len(var_7445):
            var_5246[var_4260] = var_7445[var_4587]
            var_4587 += 1
            var_4260 += 1


var_5246 = [10, 7, 8, 9, 1, 5]
var_6989(var_5246)
print(var_5246)
import math

# Comment 26