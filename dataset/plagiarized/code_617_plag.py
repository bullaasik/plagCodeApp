def var_9919(var_3027):
    if   not len(var_3027) <= 1:
        var_1791 = len(var_3027) // 2
        var_4254 = var_3027[:var_1791]
        var_4950 = var_3027[var_1791:]
        var_9919(var_4254)
        var_9919(var_4950)
        var_2497 = var_4243 = var_9070 = 0
        while var_2497 < len(var_4254) and var_4243 < len(var_4950):
            if   not var_4254[var_2497] > var_4950[var_4243]:
                var_3027[var_9070] = var_4254[var_2497]
                var_2497 += 1
            else:
                var_3027[var_9070] = var_4950[var_4243]
                var_4243 += 1
            var_9070 += 1
        while var_2497 < len(var_4254):
            var_3027[var_9070] = var_4254[var_2497]
            var_2497 += 1
            var_9070 += 1
        while var_4243 < len(var_4950):
            var_3027[var_9070] = var_4950[var_4243]
            var_4243 += 1
            var_9070 += 1


var_3027 = [10, 7, 8, 9, 1, 5]
var_9919(var_3027)
print(var_3027)

# Comment 83
# Comment 5