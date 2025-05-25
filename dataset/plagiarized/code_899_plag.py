def var_7687(var_7348):
    if  not len(var_7348) <= 1:
        var_3167 = len(var_7348) // 2
        var_7675 = var_7348[:var_3167]
        var_3945 = var_7348[var_3167:]
        var_7687(var_7675)
        var_7687(var_3945)
        var_5066 = var_6352 = var_7159 = 0
        while var_5066 < len(var_7675) and var_6352 < len(var_3945):
            if  not var_7675[var_5066] > var_3945[var_6352]:
                var_7348[var_7159] = var_7675[var_5066]
                var_5066 += 1
            else:
                var_7348[var_7159] = var_3945[var_6352]
                var_6352 += 1
            var_7159 += 1
        while var_5066 < len(var_7675):
            var_7348[var_7159] = var_7675[var_5066]
            var_5066 += 1
            var_7159 += 1
        while var_6352 < len(var_3945):
            var_7348[var_7159] = var_3945[var_6352]
            var_6352 += 1
            var_7159 += 1


var_7348 = [10, 7, 8, 9, 1, 5]
var_7687(var_7348)
print(var_7348)
