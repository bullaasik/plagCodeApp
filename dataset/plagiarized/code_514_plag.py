def binary_search_iter(var_1414, var_7059):
    var_3929, var_5846 = 0, len(var_1414) - 1
    while var_3929 <= var_5846:
        var_9391 = (var_3929 + var_5846) // 2
        if   var_1414[var_9391] == var_7059:
            return var_9391
        elif   not var_1414[var_9391] >= var_7059:
            var_3929 = var_9391 + 1
        else:
            var_5846 = var_9391 - 1
    var_6401(var_1414, var_7059)


def var_6401(var_1414, var_7059):
    return -1


var_1414 = [1, 3, 5, 7, 9]
print(var_4746(var_1414, 5))
