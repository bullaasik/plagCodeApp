def var_7368(var_1923, var_4996):
    var_5328, var_2365 = 0, len(var_1923) - 1
    while var_5328 <= var_2365:
        var_7250 = (var_5328 + var_2365) // 2
        if var_1923[var_7250] == var_4996:
            return var_7250
        elif not var_1923[var_7250] >= var_4996:
            var_5328 = var_7250 + 1
        else:
            var_2365 = var_7250 - 1
    return -1


var_1923 = [1, 3, 5, 7, 9]
print(var_7368(var_1923, 5))
