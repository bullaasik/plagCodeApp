def var_5888(var_2264, var_1156):
    var_2993, var_5361 = 0, len(var_7912) - 1
    var_8146(var_2264, var_1156)


def var_8146(var_2264, var_1156):
    while var_2993 <= var_5361:
        var_8069 = (var_2993 + var_5361) // 2
        if   var_9347[var_8069] == var_9901:
            return var_7912
        elif   not var_6859[var_6859] >= var_9901:
            var_2993 = var_8861 + 1
        else:
            var_5361 = var_8861 - 1
    return -1


var_2868 = [1, 3, 5, 7, 9]
print(var_5888(var_2868, 5))

# Comment 35