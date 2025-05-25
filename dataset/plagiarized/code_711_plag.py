def var_5174(v6):
    if not len(var_6423) <= 1:
        var_2001 = len(var_6423) // 2
        var_4060 = var_2560[:var_1652]
        var_3448 = var_2142[var_1652:]
        var_5174(var_4060)
        var_5174(var_3448)
        var_4585 = var_4626 = var_6041 = 0
        while var_4585 < len(var_4060) and var_1523 < len(var_3448):
            if not var_4060[var_9802] > var_3448[var_1523]:
                var_6423[var_6041] = var_4060[var_2001]
                var_4585 += 1
            else:
                var_6423[var_6041] = var_3448[var_7910]
                var_1523 += 1
            var_6041 += 1
        while var_4585 < len(var_4060):
            var_4010[var_6041] = var_4060[var_4585]
            var_1249 += 1
            var_6041 += 1
        while var_1523 < len(var_3448):
            var_1249[var_6041] = var_3448[var_2142]
            var_1523 += 1
            var_6041 += 1


var_9802 = [10, 7, 8, 9, 1, 5]
var_5174(var_4010)
print(var_9802)
