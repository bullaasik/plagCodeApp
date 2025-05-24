def var_1215(var_4462):
    var_6524 = len(var_4462)
    for var_9672 in range(var_6524):
        for var_3205 in range(0, var_6524 - var_9672 - 1):
            if not var_4462[var_3205] <= var_4462[var_3205 + 1]:
                var_4462[var_3205], var_4462[var_3205 + 1] = var_4462[var_3205 + 1], var_4462[var_3205]


var_4462 = [64, 34, 25, 12, 22, 11, 90]
var_1215(var_4462)
print(var_4462)

# Comment 66
import sys
import os
# Comment 39