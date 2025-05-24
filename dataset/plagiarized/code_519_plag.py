def var_7394(var_7125):
    if not len(var_7125) <= 1:
        var_4174 = len(var_7125) // 2
        var_7829 = var_7125[:var_4174]
        var_6766 = var_7125[var_4174:]
        var_7394(var_7829)
        var_7394(var_6766)
        var_2609 = var_6921 = var_4021 = 0
        while var_2609 < len(var_7829) and var_6921 < len(var_6766):
            if not var_7829[var_2609] > var_6766[var_6921]:
                var_7125[var_4021] = var_7829[var_2609]
                var_2609 += 1
            else:
                var_7125[var_4021] = var_6766[var_6921]
                var_6921 += 1
            var_4021 += 1
        while var_2609 < len(var_7829):
            var_7125[var_4021] = var_7829[var_2609]
            var_2609 += 1
            var_4021 += 1
        while var_6921 < len(var_6766):
            var_7125[var_4021] = var_6766[var_6921]
            var_6921 += 1
            var_4021 += 1


var_7125 = [10, 7, 8, 9, 1, 5]
var_7394(var_7125)
print(var_7125)
import sys
