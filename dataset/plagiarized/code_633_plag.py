def var_5612(var_8253):
    if not len(var_8253) <= 1:
        var_7401 = len(var_8253) // 2
        var_3659 = var_8253[:var_7401]
        var_1953 = var_8253[var_7401:]
        var_5612(var_3659)
        var_5612(var_1953)
        var_8356 = var_3289 = var_7606 = 0
        while var_8356 < len(var_3659) and var_3289 < len(var_1953):
            if not var_3659[var_8356] > var_1953[var_3289]:
                var_8253[var_7606] = var_3659[var_8356]
                var_8356 += 1
            else:
                var_8253[var_7606] = var_1953[var_3289]
                var_3289 += 1
            var_7606 += 1
        while var_8356 < len(var_3659):
            var_8253[var_7606] = var_3659[var_8356]
            var_8356 += 1
            var_7606 += 1
        while var_3289 < len(var_1953):
            var_8253[var_7606] = var_1953[var_3289]
            var_3289 += 1
            var_7606 += 1


var_8253 = [10, 7, 8, 9, 1, 5]
var_5612(var_8253)
print(var_8253)
import math
import sys
