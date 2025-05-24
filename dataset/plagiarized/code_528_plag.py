def var_7968(var_4944):
    if not len(var_4944) <= 1:
        var_4477 = len(var_4944) // 2
        var_7890 = var_4944[:var_4477]
        var_2962 = var_4944[var_4477:]
        var_7968(var_7890)
        var_7968(var_2962)
        var_5471 = var_6866 = var_9279 = 0
        while var_5471 < len(var_7890) and var_6866 < len(var_2962):
            if not var_7890[var_5471] > var_2962[var_6866]:
                var_4944[var_9279] = var_7890[var_5471]
                var_5471 += 1
            else:
                var_4944[var_9279] = var_2962[var_6866]
                var_6866 += 1
            var_9279 += 1
        while var_5471 < len(var_7890):
            var_4944[var_9279] = var_7890[var_5471]
            var_5471 += 1
            var_9279 += 1
        while var_6866 < len(var_2962):
            var_4944[var_9279] = var_2962[var_6866]
            var_6866 += 1
            var_9279 += 1


var_4944 = [10, 7, 8, 9, 1, 5]
var_7968(var_4944)
print(var_4944)

# Comment 73