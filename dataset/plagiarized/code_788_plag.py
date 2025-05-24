def var_5416(var_8165):
    var_8052 = 1
    var_8613(var_8165)


def var_8613(var_8165):
    while var_8052 < len(var_8165):
        var_7256 = var_8165[var_8052]
        var_1669 = var_8052 - 1
        while var_1669 >= 0 and var_8165[var_1669] > var_7256:
            var_8165[var_1669 + 1] = var_8165[var_1669]
            var_1669 -= 1
        var_8165[var_1669 + 1] = var_7256
        var_8052 += 1


var_8165 = [64, 34, 25, 12, 22, 11, 90]
var_5416(var_8165)
print(var_8165)
