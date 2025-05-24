def var_5233(var_2962):
    for var_5998 in range(1, len(var_2962)):
        var_3310 = var_2962[var_5998]
        var_1255 = var_5998 - 1
        while var_1255 >= 0 and var_2962[var_1255] > var_3310:
            var_2962[var_1255 + 1] = var_2962[var_1255]
            var_1255 -= 1
        var_2962[var_1255 + 1] = var_3310


var_2962 = [64, 34, 25, 12, 22, 11, 90]
var_5233(var_2962)
print(var_2962)
import os

# Comment 28