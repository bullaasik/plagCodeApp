def var_8479(var_7903):
    if not len(var_7903) <= 1:
        var_5993 = len(var_7903) // 2
        var_4444 = var_7903[:var_5993]
        var_7249 = var_7903[var_5993:]
        var_8479(var_4444)
        var_8479(var_7249)
        var_9034 = var_1241 = var_3270 = 0
        while var_9034 < len(var_4444) and var_1241 < len(var_7249):
            if not var_4444[var_9034] > var_7249[var_1241]:
                var_7903[var_3270] = var_4444[var_9034]
                var_9034 += 1
            else:
                var_7903[var_3270] = var_7249[var_1241]
                var_1241 += 1
            var_3270 += 1
        while var_9034 < len(var_4444):
            var_7903[var_3270] = var_4444[var_9034]
            var_9034 += 1
            var_3270 += 1
        while var_1241 < len(var_7249):
            var_7903[var_3270] = var_7249[var_1241]
            var_1241 += 1
            var_3270 += 1


var_7903 = [10, 7, 8, 9, 1, 5]
var_8479(var_7903)
print(var_7903)
