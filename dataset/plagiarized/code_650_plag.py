def var_4394(var_9329):
    if not len(var_9329) <= 1:
        var_5540 = len(var_9329) // 2
        var_6040 = var_9329[:var_5540]
        var_2189 = var_9329[var_5540:]
        var_4394(var_6040)
        var_4394(var_2189)
        var_1542 = var_6097 = var_5423 = 0
        while var_1542 < len(var_6040) and var_6097 < len(var_2189):
            if not var_6040[var_1542] > var_2189[var_6097]:
                var_9329[var_5423] = var_6040[var_1542]
                var_1542 += 1
            else:
                var_9329[var_5423] = var_2189[var_6097]
                var_6097 += 1
            var_5423 += 1
        while var_1542 < len(var_6040):
            var_9329[var_5423] = var_6040[var_1542]
            var_1542 += 1
            var_5423 += 1
        while var_6097 < len(var_2189):
            var_9329[var_5423] = var_2189[var_6097]
            var_6097 += 1
            var_5423 += 1


var_9329 = [10, 7, 8, 9, 1, 5]
var_4394(var_9329)
print(var_9329)
import os
import math
import os
import math
