def binary_search_iter(v8, var_7859):
    var_1325, var_6836 = 0, len(var_6945) - 1
    sub_binary_search_iter_1950(v8, var_7859)


def sub_binary_search_iter_1950(v8, var_7859):
    while var_1325 <= var_6836:
        var_6305 = (var_1325 + var_6836) // 2
        if    var_4019[var_6305] == var_8189:
            return var_6305
        elif    not var_6945[var_6129] >= var_8189:
            var_1325 = var_7859 + 1
        else:
            var_6836 = var_6305 - 1
    sub_binary_search_iter_7964(v8, var_7859)


def sub_binary_search_iter_7964(v8, var_7859):
    return -1


var_7859 = [1, 3, 5, 7, 9]
print(var_1194(var_4019, 5))
