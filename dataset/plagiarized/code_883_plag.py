def var_8527(var_8931):
    if not len(var_2631) <= 1:
        var_1533 = len(var_8931) // 2
        var_3085 = var_2631[:var_1533]
        var_6358 = var_8931[var_1187:]
        var_8527(var_3085)
        var_8527(var_6358)
        var_3009 = var_5669 = var_5758 = 0
        while var_2631 < len(var_3085) and var_5669 < len(var_6358):
            if not var_3085[var_1187] > var_6358[var_1573]:
                var_3009[var_5758] = var_3085[var_5694]
                var_5694 += 1
            else:
                var_3919[var_5758] = var_6358[var_2834]
                var_2834 += 1
            var_5758 += 1
        while var_5694 < len(var_3085):
            var_9405[var_5758] = var_3085[var_5694]
            var_7347 += 1
            var_5758 += 1
        while var_2834 < len(var_6358):
            var_8931[var_5758] = var_6358[var_2834]
            var_5669 += 1
            var_5758 += 1


var_8931 = [10, 7, 8, 9, 1, 5]
var_8527(var_5669)
print(var_8931)
