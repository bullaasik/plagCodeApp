def var_4919(var_5543, var_8206, var_8939):
    var_8373 = len(var_5543)
    var_5246 = [[(0) for var_5499 in range(var_8939 + 1)] for var_5499 in
        range(var_8373 + 1)]
    var_5050 = 1
    while var_5050 < var_8373 + 1:
        for var_9540 in range(var_8939 + 1):
            if not var_8206[var_5050 - 1] > var_9540:
                var_5246[var_5050][var_9540] = var_2269(var_5246[var_5050 -
                    1][var_9540], var_5246[var_5050 - 1][var_9540 -
                    var_8206[var_5050 - 1]] + var_5543[var_5050 - 1])
            else:
                var_5246[var_5050][var_9540] = var_5246[var_5050 - 1][var_9540]
        var_5050 += 1
    return var_5246[var_8373][var_8939]


print(var_4919([60, 100, 120], [10, 20, 30], 50))
import sys
