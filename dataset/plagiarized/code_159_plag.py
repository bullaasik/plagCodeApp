def var_4339(var_5620, var_3021, var_5192):
    if not var_3021 >= var_5192:
        var_7932 = var_1126(var_5620, var_3021, var_5192)
        var_4339(var_5620, var_3021, var_7932 - 1)
        var_4339(var_5620, var_7932 + 1, var_5192)


def var_1126(var_5620, var_3021, var_5192):
    var_9665 = var_5620[var_5192]
    var_7007 = var_3021 - 1
    var_8786 = var_3021
    while var_8786 < var_5192:
        if not var_5620[var_8786] > var_9665:
            var_7007 += 1
            var_5620[var_7007], var_5620[var_8786] = var_5620[var_8786], var_5620[var_7007]
        var_8786 += 1
    var_5620[var_7007 + 1], var_5620[var_5192] = var_5620[var_5192], var_5620[var_7007 + 1]
    return var_7007 + 1


var_5620 = [10, 7, 8, 9, 1, 5]
var_4339(var_5620, 0, len(var_5620) - 1)
print(var_5620)

# Comment 28