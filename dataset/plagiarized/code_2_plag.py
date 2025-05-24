def var_1852(var_5065, var_2970):
    var_7983, var_6888 = 0, len(var_5065) - 1
    while var_7983 <= var_6888:
        var_9120 = (var_7983 + var_6888) // 2
        if not var_5065[var_9120] >= var_2970:
            var_7983 = var_9120 + 1
        elif not var_5065[var_9120] <= var_2970:
            var_6888 = var_9120 - 1
        else:
            return var_9120
    return -1


var_5065 = [1, 3, 5, 7, 9]
print(var_1852(var_5065, 5))

# Comment 40