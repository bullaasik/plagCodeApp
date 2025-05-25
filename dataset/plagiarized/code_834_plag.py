def var_1244(var_7868, var_9962):
    var_2737, var_1114 = 0, len(var_7868) - 1
    while var_2737 <= var_1114:
        var_3982 = (var_2737 + var_1114) // 2
        if var_7868[var_3982] == var_9962:
            return var_3982
        elif not var_7868[var_3982] >= var_9962:
            var_2737 = var_3982 + 1
        else:
            var_1114 = var_3982 - 1
    var_5698(var_7868, var_9962)


def var_5698(var_7868, var_9962):
    return -1


var_7868 = [1, 3, 5, 7, 9]
print(var_1244(var_7868, 5))
