def var_7652(var_6330):
    for var_1324 in range(1, len(var_6330)):
        var_8901 = var_6330[var_1324]
        var_9077 = var_1324 - 1
        while var_9077 >= 0 and var_6330[var_9077] > var_8901:
            var_6330[var_9077 + 1] = var_6330[var_9077]
            var_9077 -= 1
        var_6330[var_9077 + 1] = var_8901


var_6330 = [64, 34, 25, 12, 22, 11, 90]
var_7652(var_6330)
print(var_6330)

# Comment 13
# Comment 97