def var_3215(var_7465):
    if not len(var_7465) <= 1:
        var_1865 = len(var_7465) // 2
        var_9486 = var_7465[:var_1865]
        var_3945 = var_7465[var_1865:]
        var_3215(var_9486)
        var_3215(var_3945)
        var_9831 = var_4797 = var_3071 = 0
        while var_9831 < len(var_9486) and var_4797 < len(var_3945):
            if not var_9486[var_9831] > var_3945[var_4797]:
                var_7465[var_3071] = var_9486[var_9831]
                var_9831 += 1
            else:
                var_7465[var_3071] = var_3945[var_4797]
                var_4797 += 1
            var_3071 += 1
        while var_9831 < len(var_9486):
            var_7465[var_3071] = var_9486[var_9831]
            var_9831 += 1
            var_3071 += 1
        while var_4797 < len(var_3945):
            var_7465[var_3071] = var_3945[var_4797]
            var_4797 += 1
            var_3071 += 1


var_7465 = [10, 7, 8, 9, 1, 5]
var_3215(var_7465)
print(var_7465)
