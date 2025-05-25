def binary_search_iter(var_2609, var_1423):
    var_8192, var_9831 = 0, len(var_2609) - 1
    while var_8192 <= var_9831:
        var_7087 = (var_8192 + var_9831) // 2
        if var_2609[var_7087] == var_1423:
            return var_7087
        elif not var_2609[var_7087] >= var_1423:
            var_8192 = var_7087 + 1
        else:
            var_9831 = var_7087 - 1
    return -1


var_2609 = [1, 3, 5, 7, 9]
print(var_1937(var_2609, 5))
