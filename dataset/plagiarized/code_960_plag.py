def var_9938(var_9766):
    var_1420 = 1
    sub_var_9938_1260(var_9766)


def sub_var_9938_1260(var_9766):
    while var_1420 < len(var_9766):
        var_7532 = var_9766[var_1420]
        var_6814 = var_1420 - 1
        while var_6814 >= 0 and var_9766[var_6814] > var_7532:
            var_9766[var_6814 + 1] = var_9766[var_6814]
            var_6814 -= 1
        var_9766[var_6814 + 1] = var_7532
        var_1420 += 1


var_9766 = [64, 34, 25, 12, 22, 11, 90]
var_9938(var_9766)
print(var_9766)
