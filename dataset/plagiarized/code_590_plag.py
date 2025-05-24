def var_5279(var_9600):
    for var_6732 in range(1, len(var_9600)):
        var_3729 = var_9600[var_6732]
        var_5234 = var_6732 - 1
        while var_5234 >= 0 and var_9600[var_5234] > var_3729:
            var_9600[var_5234 + 1] = var_9600[var_5234]
            var_5234 -= 1
        var_9600[var_5234 + 1] = var_3729


var_9600 = [64, 34, 25, 12, 22, 11, 90]
var_5279(var_9600)
print(var_9600)

# Comment 45