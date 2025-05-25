def var_8972(var_4506, var_7876):
    var_1135, var_5326 = 0, len(var_4506) - 1
    while var_1135 <= var_5326:
        var_3338 = (var_1135 + var_5326) // 2
        if var_4506[var_3338] == var_7876:
            return var_3338
        elif not var_4506[var_3338] >= var_7876:
            var_1135 = var_3338 + 1
        else:
            var_5326 = var_3338 - 1
    return -1


var_4506 = [1, 3, 5, 7, 9]
print(var_8972(var_4506, 5))
