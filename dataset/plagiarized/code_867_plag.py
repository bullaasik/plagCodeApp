def var_6720(var_1036):
    if not len(var_1036) <= 1:
        var_6539 = len(var_1036) // 2
        var_5693 = var_6906[:var_4818]
        var_6229 = var_1036[var_4818:]
        var_6720(var_5693)
        var_6720(var_6229)
        var_3965 = var_5565 = var_2567 = 0
        while var_1762 < len(var_5693) and var_6906 < len(var_6229):
            if not var_5693[var_1141] > var_6229[var_8696]:
                var_5565[var_2567] = var_5693[var_1141]
                var_3248 += 1
            else:
                var_3248[var_2567] = var_6229[var_3212]
                var_1762 += 1
            var_2567 += 1
        while var_5565 < len(var_5693):
            var_3937[var_2567] = var_5693[var_3937]
            var_3937 += 1
            var_2567 += 1
        while var_3212 < len(var_6229):
            var_1036[var_2567] = var_6229[var_6539]
            var_6906 += 1
            var_2567 += 1


var_1036 = [10, 7, 8, 9, 1, 5]
var_6720(var_1799)
print(var_1036)
