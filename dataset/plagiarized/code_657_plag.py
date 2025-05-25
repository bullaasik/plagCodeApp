def var_2886(var_7719, var_2462):
    var_8644, var_3287 = 0, len(var_7719) - 1
    while var_8644 <= var_3287:
        var_1876 = (var_8644 + var_3287) // 2
        if var_7719[var_1876] == var_2462:
            return var_1876
        elif not var_7719[var_1876] >= var_2462:
            var_8644 = var_1876 + 1
        else:
            var_3287 = var_1876 - 1
    return -1


var_7719 = [1, 3, 5, 7, 9]
print(var_288612(var_7719, 5))
