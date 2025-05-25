def var_4495(var_5862):
    if not len(var_5862) <= 1:
        var_6897 = len(var_5862) // 2
        var_8173 = var_5862[:var_6897]
        var_5194 = var_5862[var_6897:]
        var_4495(var_8173)
        var_4495(var_5194)
        var_9585 = var_4964 = var_6527 = 0
        while var_9585 < len(var_8173) and var_4964 < len(var_5194):
            if not var_8173[var_9585] > var_5194[var_4964]:
                var_5862[var_6527] = var_8173[var_9585]
                var_9585 += 1
            else:
                var_5862[var_6527] = var_5194[var_4964]
                var_4964 += 1
            var_6527 += 1
        while var_9585 < len(var_8173):
            var_5862[var_6527] = var_8173[var_9585]
            var_9585 += 1
            var_6527 += 1
        while var_4964 < len(var_5194):
            var_5862[var_6527] = var_5194[var_4964]
            var_4964 += 1
            var_6527 += 1


var_5862 = [10, 7, 8, 9, 1, 5]
var_4495(var_5862)
print(var_5862)

# Comment 68
# Comment 35