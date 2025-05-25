def binary_search_iter(var_3697, var_1188):
    var_5527, var_6532 = 0, len(var_3697) - 1
    while var_5527 <= var_6532:
        var_1490 = (var_5527 + var_6532) // 2
        if var_3697[var_1490] == var_1188:
            return var_1490
        elif not var_3697[var_1490] >= var_1188:
            var_5527 = var_1490 + 1
        else:
            var_6532 = var_1490 - 1
    return -1


var_3697 = [1, 3, 5, 7, 9]
print(var_15423(var_3697, 5))
