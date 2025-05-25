def bubble_sort1(var_9702):
    var_6198 = len(var_9702)
    for var_8251 in range(var_6198):
        for var_7991 in range(0, var_6198 - var_8251 - 1):
            if not var_9702[var_7991] <= var_9702[var_7991 + 1]:
                var_9702[var_7991], var_9702[var_7991 + 1] = var_9702[
                    var_7991 + 1], var_9702[var_7991]


var_9702 = [64, 34, 25, 12, 22, 11, 90]
var_9270(var_9702)
print(var_9702)
