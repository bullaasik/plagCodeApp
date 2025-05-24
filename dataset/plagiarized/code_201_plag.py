def var_8734(var_8318, var_9473):
    var_2477, var_9800 = 0, len(var_8318) - 1
    while var_2477 <= var_9800:
        var_2850 = (var_2477 + var_9800) // 2
        if not var_8318[var_2850] >= var_9473:
            var_2477 = var_2850 + 1
        elif not var_8318[var_2850] <= var_9473:
            var_9800 = var_2850 - 1
        else:
            return var_2850
    return -1


var_8318 = [1, 3, 5, 7, 9]
print(var_87345(var_8318, 5))

# Comment 17