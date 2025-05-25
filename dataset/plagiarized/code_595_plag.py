def var_2069(var_9676):
    if not len(var_9676) <= 1:
        var_8445 = len(var_9676) // 2
        var_6699 = var_9676[:var_8445]
        var_5967 = var_9676[var_8445:]
        var_2069(var_6699)
        var_2069(var_5967)
        var_4675 = var_8362 = var_4291 = 0
        while var_4675 < len(var_6699) and var_8362 < len(var_5967):
            if not var_6699[var_4675] > var_5967[var_8362]:
                var_9676[var_4291] = var_6699[var_4675]
                var_4675 += 1
            else:
                var_9676[var_4291] = var_5967[var_8362]
                var_8362 += 1
            var_4291 += 1
        while var_4675 < len(var_6699):
            var_9676[var_4291] = var_6699[var_4675]
            var_4675 += 1
            var_4291 += 1
        while var_8362 < len(var_5967):
            var_9676[var_4291] = var_5967[var_8362]
            var_8362 += 1
            var_4291 += 1


var_9676 = [10, 7, 8, 9, 1, 5]
var_2069(var_9676)
print(var_9676)
import sys
import sys
import sys

import sys
import os