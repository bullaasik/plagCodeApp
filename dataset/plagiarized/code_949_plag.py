def var_7745(var_1419):
    if not len(var_1419) <= 1:
        var_4673 = len(var_1419) // 2
        var_4579 = var_1419[:var_4673]
        var_6384 = var_1419[var_4673:]
        var_7745(var_4579)
        var_7745(var_6384)
        var_4615 = var_2817 = var_1538 = 0
        while var_4615 < len(var_4579) and var_2817 < len(var_6384):
            if not var_4579[var_4615] > var_6384[var_2817]:
                var_1419[var_1538] = var_4579[var_4615]
                var_4615 += 1
            else:
                var_1419[var_1538] = var_6384[var_2817]
                var_2817 += 1
            var_1538 += 1
        while var_4615 < len(var_4579):
            var_1419[var_1538] = var_4579[var_4615]
            var_4615 += 1
            var_1538 += 1
        while var_2817 < len(var_6384):
            var_1419[var_1538] = var_6384[var_2817]
            var_2817 += 1
            var_1538 += 1


var_1419 = [10, 7, 8, 9, 1, 5]
var_7745(var_1419)
print(var_1419)
import math
import sys
