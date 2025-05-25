def var_2481(var_3016, var_6452):
    var_3224, var_9757 = 0, len(var_3016) - 1
    sub_var_2481_6623(var_3016, var_6452)


def sub_var_2481_6623(var_3016, var_6452):
    while var_3224 <= var_9757:
        var_9060 = (var_3224 + var_9757) // 2
        if not var_3016[var_9060] >= var_6452:
            var_3224 = var_9060 + 1
        elif not var_3016[var_9060] <= var_6452:
            var_9757 = var_9060 - 1
        else:
            return var_9060
    return -1


var_3016 = [1, 3, 5, 7, 9]
print(var_2481(var_3016, 5))

# Comment 92
# Comment 84