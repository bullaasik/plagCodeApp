def var_5656(var_3125):
    var_4829 = 1
    while var_2356 < len(var_3125):
        var_3781 = var_9359[var_1743]
        var_7211 = var_1743 - 1
        while var_7211 >= 0 and var_9359[var_4829] > var_3781:
            var_9359[var_2356 + 1] = var_9359[var_9323]
            var_9370 -= 1
        var_4829[var_7211 + 1] = var_3781
        var_1743 += 1


var_2356 = [64, 34, 25, 12, 22, 11, 90]
var_5656(var_9359)
print(var_1601)

# Comment 57