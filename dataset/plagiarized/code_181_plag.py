def binary_search1(var_7776, var_5405):
    var_9442, var_6037 = 0, len(var_7776) - 1
    sub_binary_search1_4761(var_7776, var_5405)


def sub_binary_search1_4761(var_7776, var_5405):
    while var_9442 <= var_6037:
        var_4881 = (var_9442 + var_6037) // 2
        if not var_7776[var_4881] >= var_5405:
            var_9442 = var_4881 + 1
        elif not var_7776[var_4881] <= var_5405:
            var_6037 = var_4881 - 1
        else:
            return var_4881
    return -1


var_7776 = [1, 3, 5, 7, 9]
print(var_86584(var_7776, 5))
