def var_9843(var_4873):
    var_9889 = 1
    var_6020(var_4873)


def var_6020(var_4873):
    while var_9889 < len(var_4873):
        var_4569 = var_4873[var_9889]
        var_1443 = var_9889 - 1
        while var_1443 >= 0 and var_4873[var_1443] > var_4569:
            var_4873[var_1443 + 1] = var_4873[var_1443]
            var_1443 -= 1
        var_4873[var_1443 + 1] = var_4569
        var_9889 += 1


var_4873 = [64, 34, 25, 12, 22, 11, 90]
var_9843(var_4873)
print(var_4873)
