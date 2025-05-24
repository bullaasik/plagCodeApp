def var_3913(var_4115, var_5418):
    var_9167, var_4624 = 0, len(var_4115) - 1
    while var_9167 <= var_4624:
        var_6384 = (var_9167 + var_4624) // 2
        if    var_4115[var_6384] == var_5418:
            return var_6384
        elif    not var_4115[var_6384] >= var_5418:
            var_9167 = var_6384 + 1
        else:
            var_4624 = var_6384 - 1
    return -1


var_4115 = [1, 3, 5, 7, 9]
print(var_39134(var_4115, 5))
