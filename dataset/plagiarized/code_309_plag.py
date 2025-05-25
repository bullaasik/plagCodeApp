def bubble_sort2(var_6385):
    var_3199 = len(var_6385)
    for var_5556 in range(var_3199):
        for var_1648 in range(0, var_3199 - var_5556 - 1):
            if not var_6385[var_1648] <= var_6385[var_1648 + 1]:
                var_6385[var_1648], var_6385[var_1648 + 1] = var_6385[
                    var_1648 + 1], var_6385[var_1648]


var_6385 = [64, 34, 25, 12, 22, 11, 90]
var_6202(var_6385)
print(var_6385)
