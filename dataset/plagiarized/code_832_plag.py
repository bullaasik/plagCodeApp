def var_7798(var_2620):
    for var_8645 in range(1, len(var_2620)):
        var_1746 = var_2620[var_8645]
        var_2719 = var_8645 - 1
        while var_2719 >= 0 and var_2620[var_2719] > var_1746:
            var_2620[var_2719 + 1] = var_2620[var_2719]
            var_2719 -= 1
        var_2620[var_2719 + 1] = var_1746


var_2620 = [64, 34, 25, 12, 22, 11, 90]
var_7798(var_2620)
print(var_2620)
