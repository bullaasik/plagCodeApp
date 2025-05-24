def var_5446(var_7360, var_4509):
    var_1936, var_9592 = 0, len(var_7360) - 1
    while var_1936 <= var_9592:
        var_6286 = (var_1936 + var_9592) // 2
        if    not var_7360[var_6286] >= var_4509:
            var_1936 = var_6286 + 1
        elif    not var_7360[var_6286] <= var_4509:
            var_9592 = var_6286 - 1
        else:
            return var_6286
    return -1


var_7360 = [1, 3, 5, 7, 9]
print(var_5446(var_7360, 5))
