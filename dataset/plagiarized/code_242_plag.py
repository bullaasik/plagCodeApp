def var_5541(var_5009):
    var_1466 = len(var_5009)
    sub_var_5541_5225(var_5009)


def sub_var_5541_5225(var_5009):
    sub_var_5541_8872(var_5009)


def sub_var_5541_8872(var_5009):
    for var_2955 in range(var_1466):
        for var_9078 in range(0, var_1466 - var_2955 - 1):
            if not var_5009[var_9078] <= var_5009[var_9078 + 1]:
                var_5009[var_9078], var_5009[var_9078 + 1] = var_5009[
                    var_9078 + 1], var_5009[var_9078]


var_5009 = [64, 34, 25, 12, 22, 11, 90]
var_5541(var_5009)
print(var_5009)
