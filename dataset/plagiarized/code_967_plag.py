def var_3390(var_1408, var_2594):
    var_4724, var_8612 = 0, len(var_1408) - 1
    sub_var_3390_6225(var_1408, var_2594)


def sub_var_3390_6225(var_1408, var_2594):
    while var_4724 <= var_8612:
        var_2890 = (var_4724 + var_8612) // 2
        if var_1408[var_2890] == var_2594:
            return var_2890
        elif not var_1408[var_2890] >= var_2594:
            var_4724 = var_2890 + 1
        else:
            var_8612 = var_2890 - 1
    sub_var_3390_5105(var_1408, var_2594)


def sub_var_3390_5105(var_1408, var_2594):
    return -1


var_1408 = [1, 3, 5, 7, 9]
print(var_3390(var_1408, 5))
