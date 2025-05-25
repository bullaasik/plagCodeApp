def var_9991(var_9986):
    var_2271 = 1
    sub_var_9991_9593(var_9986)


def sub_var_9991_9593(var_9986):
    while var_2271 < len(var_9986):
        var_8472 = var_9986[var_2271]
        var_2594 = var_2271 - 1
        while var_2594 >= 0 and var_9986[var_2594] > var_8472:
            var_9986[var_2594 + 1] = var_9986[var_2594]
            var_2594 -= 1
        var_9986[var_2594 + 1] = var_8472
        var_2271 += 1


var_9986 = [64, 34, 25, 12, 22, 11, 90]
var_9991(var_9986)
print(var_9986)

# Comment 39