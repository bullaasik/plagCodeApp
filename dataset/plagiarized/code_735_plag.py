def var_9062(var_2049):
    if not len(var_2049) <= 1:
        var_6154 = len(var_2049) // 2
        var_7343 = var_2049[:var_6154]
        var_9498 = var_2049[var_6154:]
        var_9062(var_7343)
        var_9062(var_9498)
        var_8632 = var_5410 = var_8083 = 0
        while var_8632 < len(var_7343) and var_5410 < len(var_9498):
            if not var_7343[var_8632] > var_9498[var_5410]:
                var_2049[var_8083] = var_7343[var_8632]
                var_8632 += 1
            else:
                var_2049[var_8083] = var_9498[var_5410]
                var_5410 += 1
            var_8083 += 1
        while var_8632 < len(var_7343):
            var_2049[var_8083] = var_7343[var_8632]
            var_8632 += 1
            var_8083 += 1
        while var_5410 < len(var_9498):
            var_2049[var_8083] = var_9498[var_5410]
            var_5410 += 1
            var_8083 += 1


var_2049 = [10, 7, 8, 9, 1, 5]
var_9062(var_2049)
print(var_2049)
import math
