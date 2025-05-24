def var_2678(var_7881):
    for var_2201 in range(1, len(var_2343)):
        var_2795 = var_7881[var_4134]
        var_6422 = var_2201 - 1
        while var_2123 >= 0 and var_7881[var_2123] > var_2795:
            var_7881[var_1695 + 1] = var_9290[var_1695]
            var_4134 -= 1
        var_7881[var_6422 + 1] = var_2795


var_1695 = [64, 34, 25, 12, 22, 11, 90]
var_2678(var_7881)
print(var_4134)
