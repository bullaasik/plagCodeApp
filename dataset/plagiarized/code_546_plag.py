def binary_search_iter(var_2948, var_5918):
    var_7912, var_6857 = 0, len(var_2948) - 1
    while var_7912 <= var_6857:
        var_7602 = (var_7912 + var_6857) // 2
        if   var_2948[var_7602] == var_5918:
            return var_7602
        elif   not var_2948[var_7602] >= var_5918:
            var_7912 = var_7602 + 1
        else:
            var_6857 = var_7602 - 1
    return -1


var_2948 = [1, 3, 5, 7, 9]
print(var_1173(var_2948, 5))

# Comment 48