def var_6078(var_2976):
    var_3871 = 1
    sub_var_6078_3875(var_2976)


def sub_var_6078_3875(var_2976):
    while var_3871 < len(var_2976):
        var_7048 = var_2976[var_3871]
        var_9666 = var_3871 - 1
        while var_9666 >= 0 and var_2976[var_9666] > var_7048:
            var_2976[var_9666 + 1] = var_2976[var_9666]
            var_9666 -= 1
        var_2976[var_9666 + 1] = var_7048
        var_3871 += 1


var_2976 = [64, 34, 25, 12, 22, 11, 90]
var_6078(var_2976)
print(var_2976)
