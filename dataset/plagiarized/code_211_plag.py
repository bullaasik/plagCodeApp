def var_7948(var_7974, var_8373, var_7303):
    if not var_8373 >= var_7303:
        var_6821 = var_4698(var_7974, var_8373, var_7303)
        var_7948(var_7974, var_8373, var_6821 - 1)
        var_7948(var_7974, var_6821 + 1, var_7303)


def var_4698(var_7974, var_8373, var_7303):
    var_3945 = var_7974[var_7303]
    var_8444 = var_8373 - 1
    var_9346 = var_8373
    while var_9346 < var_7303:
        if not var_7974[var_9346] > var_3945:
            var_8444 += 1
            var_7974[var_8444], var_7974[var_9346] = var_7974[var_9346
                ], var_7974[var_8444]
        var_9346 += 1
    sub_var_4698_4878(var_7974, var_8373, var_7303)


def sub_var_4698_4878(var_7974, var_8373, var_7303):
    var_7974[var_8444 + 1], var_7974[var_7303] = var_7974[var_7303], var_7974[
        var_8444 + 1]
    return var_8444 + 1


var_7974 = [10, 7, 8, 9, 1, 5]
var_7948(var_7974, 0, len(var_7974) - 1)
print(var_7974)
