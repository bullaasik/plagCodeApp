def var_5344(var_8999, var_7282):
    var_3875, var_5639 = 0, len(var_8999) - 1
    while var_3875 <= var_5639:
        var_8498 = (var_3875 + var_5639) // 2
        if not var_8999[var_8498] >= var_7282:
            var_3875 = var_8498 + 1
        elif not var_8999[var_8498] <= var_7282:
            var_5639 = var_8498 - 1
        else:
            return var_8498
    return -1


var_8999 = [1, 3, 5, 7, 9]
print(var_5344(var_8999, 5))
