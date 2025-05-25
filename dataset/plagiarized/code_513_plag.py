def var_9797(var_2089):
    var_4004 = 1
    while var_4004 < len(var_2089):
        var_6363 = var_2089[var_4004]
        var_3742 = var_4004 - 1
        while var_3742 >= 0 and var_2089[var_3742] > var_6363:
            var_2089[var_3742 + 1] = var_2089[var_3742]
            var_3742 -= 1
        var_2089[var_3742 + 1] = var_6363
        var_4004 += 1


var_2089 = [64, 34, 25, 12, 22, 11, 90]
var_9797(var_2089)
print(var_2089)
import os

import sys
import os