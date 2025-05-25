def var_9099(var_2096):
    var_4715 = 1
    while var_4715 < len(var_2096):
        var_8501 = var_2096[var_4715]
        var_7345 = var_4715 - 1
        while var_7345 >= 0 and var_2096[var_7345] > var_8501:
            var_2096[var_7345 + 1] = var_2096[var_7345]
            var_7345 -= 1
        var_2096[var_7345 + 1] = var_8501
        var_4715 += 1


var_2096 = [64, 34, 25, 12, 22, 11, 90]
var_9099(var_2096)
print(var_2096)
