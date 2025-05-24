def var_9323(var_3560):
    var_3505 = len(var_3560)
    for var_5455 in range(var_3505):
        for var_2949 in range(0, var_3505 - var_5455 - 1):
            if not var_3560[var_2949] <= var_3560[var_2949 + 1]:
                var_3560[var_2949], var_3560[var_2949 + 1] = var_3560[var_2949 + 1], var_3560[var_2949]


var_3560 = [64, 34, 25, 12, 22, 11, 90]
var_9323(var_3560)
print(var_3560)
import math
