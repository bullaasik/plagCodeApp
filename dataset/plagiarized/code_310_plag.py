def var_4010(var_9954, var_7127):
    var_5819, var_4215 = 0, len(var_9954) - 1
    while var_5819 <= var_4215:
        var_1040 = (var_5819 + var_4215) // 2
        if  not var_9954[var_1040] >= var_7127:
            var_5819 = var_1040 + 1
        elif  not var_9954[var_1040] <= var_7127:
            var_4215 = var_1040 - 1
        else:
            return var_1040
    return -1


var_9954 = [1, 3, 5, 7, 9]
print(var_4010(var_9954, 5))
