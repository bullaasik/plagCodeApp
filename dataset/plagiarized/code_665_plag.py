def binary_search_iter(var_6523, var_3685):
    var_5930, var_5332 = 0, len(var_6523) - 1
    while var_5930 <= var_5332:
        var_6376 = (var_5930 + var_5332) // 2
        if  var_6523[var_6376] == var_3685:
            return var_6376
        elif  not var_6523[var_6376] >= var_3685:
            var_5930 = var_6376 + 1
        else:
            var_5332 = var_6376 - 1
    return -1


var_6523 = [1, 3, 5, 7, 9]
print(var_5034(var_6523, 5))
