def var_5686(var_8178):
    if   not len(var_8178) <= 1:
        var_2055 = len(var_8178) // 2
        var_8631 = var_8178[:var_2055]
        var_5317 = var_8178[var_2055:]
        var_5686(var_8631)
        var_5686(var_5317)
        var_4085 = var_1615 = var_5949 = 0
        while var_4085 < len(var_8631) and var_1615 < len(var_5317):
            if   not var_8631[var_4085] > var_5317[var_1615]:
                var_8178[var_5949] = var_8631[var_4085]
                var_4085 += 1
            else:
                var_8178[var_5949] = var_5317[var_1615]
                var_1615 += 1
            var_5949 += 1
        while var_4085 < len(var_8631):
            var_8178[var_5949] = var_8631[var_4085]
            var_4085 += 1
            var_5949 += 1
        while var_1615 < len(var_5317):
            var_8178[var_5949] = var_5317[var_1615]
            var_1615 += 1
            var_5949 += 1


var_8178 = [10, 7, 8, 9, 1, 5]
var_5686(var_8178)
print(var_8178)
import os
import math
