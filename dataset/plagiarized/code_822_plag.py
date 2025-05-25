def var_1018(var_5734):
    if not len(var_5734) <= 1:
        var_3445 = len(var_5734) // 2
        var_7407 = var_5734[:var_3445]
        var_3305 = var_5734[var_3445:]
        var_1018(var_7407)
        var_1018(var_3305)
        var_1551 = var_9697 = var_6679 = 0
        while var_1551 < len(var_7407) and var_9697 < len(var_3305):
            if not var_7407[var_1551] > var_3305[var_9697]:
                var_5734[var_6679] = var_7407[var_1551]
                var_1551 += 1
            else:
                var_5734[var_6679] = var_3305[var_9697]
                var_9697 += 1
            var_6679 += 1
        while var_1551 < len(var_7407):
            var_5734[var_6679] = var_7407[var_1551]
            var_1551 += 1
            var_6679 += 1
        while var_9697 < len(var_3305):
            var_5734[var_6679] = var_3305[var_9697]
            var_9697 += 1
            var_6679 += 1


var_5734 = [10, 7, 8, 9, 1, 5]
var_1018(var_5734)
print(var_5734)
