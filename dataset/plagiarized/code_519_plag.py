def var_6956(var_8410, var_6534):
    var_8272, var_7364 = 0, len(var_8410) - 1
    while var_8272 <= var_7364:
        var_8594 = (var_8272 + var_7364) // 2
        if var_8410[var_8594] == var_6534:
            return var_8594
        elif not var_8410[var_8594] >= var_6534:
            var_8272 = var_8594 + 1
        else:
            var_7364 = var_8594 - 1
    return -1


var_8410 = [1, 3, 5, 7, 9]
print(var_6956(var_8410, 5))
