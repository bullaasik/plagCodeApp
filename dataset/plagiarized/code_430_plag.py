def var_6089(var_7059):
    var_8811 = len(var_7059)
    var_2785 = 0
    while var_2785 < var_8811:
        for var_6446 in range(0, var_8811 - var_2785 - 1):
            if not var_7059[var_6446] <= var_7059[var_6446 + 1]:
                var_7059[var_6446], var_7059[var_6446 + 1] = var_7059[
                    var_6446 + 1], var_7059[var_6446]
        var_2785 += 1


var_7059 = [64, 34, 25, 12, 22, 11, 90]
var_6089(var_7059)
print(var_7059)
