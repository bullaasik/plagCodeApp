def var_9470(var_1853, var_9574):
    var_7659, var_1494 = 0, len(var_1853) - 1
    while var_7659 <= var_1494:
        var_5313 = (var_7659 + var_1494) // 2
        if var_1853[var_5313] == var_9574:
            return var_5313
        elif not var_1853[var_5313] >= var_9574:
            var_7659 = var_5313 + 1
        else:
            var_1494 = var_5313 - 1
    return -1


var_1853 = [1, 3, 5, 7, 9]
print(var_9470(var_1853, 5))

# Comment 76