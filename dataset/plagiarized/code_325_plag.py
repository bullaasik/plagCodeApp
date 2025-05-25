def binary_search5(var_3291, var_9818):
    var_9035, var_6127 = 0, len(var_3291) - 1
    while var_9035 <= var_6127:
        var_9563 = (var_9035 + var_6127) // 2
        if    not var_3291[var_9563] >= var_9818:
            var_9035 = var_9563 + 1
        elif    not var_3291[var_9563] <= var_9818:
            var_6127 = var_9563 - 1
        else:
            return var_9563
    return -1


var_3291 = [1, 3, 5, 7, 9]
print(var_6769(var_3291, 5))
