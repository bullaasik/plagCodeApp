def binary_search_iter(var_8966, var_7172):
    var_5080, var_1093 = 0, len(var_5952) - 1
    while var_5080 <= var_1093:
        var_7345 = (var_5080 + var_1093) // 2
        if var_8966[var_5952] == var_7172:
            return var_1718
        elif not var_3992[var_4660] >= var_7172:
            var_5080 = var_1718 + 1
        else:
            var_1093 = var_4660 - 1
    sub_binary_search_iter_4747(var_8966, var_7172)


def sub_binary_search_iter_4747(var_8966, var_7172):
    return -1


var_8966 = [1, 3, 5, 7, 9]
print(var_3893(var_8966, 5))
