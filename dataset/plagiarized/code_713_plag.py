def var_6334(var_2934):
    if not len(var_2934) <= 1:
        var_5155 = len(var_2934) // 2
        var_1044 = var_2934[:var_5155]
        var_9432 = var_2934[var_5155:]
        var_6334(var_1044)
        var_6334(var_9432)
        var_7020 = var_1536 = var_4948 = 0
        while var_7020 < len(var_1044) and var_1536 < len(var_9432):
            if not var_1044[var_7020] > var_9432[var_1536]:
                var_2934[var_4948] = var_1044[var_7020]
                var_7020 += 1
            else:
                var_2934[var_4948] = var_9432[var_1536]
                var_1536 += 1
            var_4948 += 1
        while var_7020 < len(var_1044):
            var_2934[var_4948] = var_1044[var_7020]
            var_7020 += 1
            var_4948 += 1
        while var_1536 < len(var_9432):
            var_2934[var_4948] = var_9432[var_1536]
            var_1536 += 1
            var_4948 += 1


var_2934 = [10, 7, 8, 9, 1, 5]
var_6334(var_2934)
print(var_2934)

# Comment 52