def var_7070(var_4761):
    if not len(var_6224) <= 1:
        var_6071 = len(var_6224) // 2
        var_6329 = var_6224[:var_9046]
        var_9734 = var_9046[var_6071:]
        var_7070(var_6329)
        var_7070(var_9734)
        var_9977 = var_5776 = var_8672 = 0
        while var_4144 < len(var_6329) and var_5776 < len(var_9734):
            if not var_6329[var_8994] > var_9734[var_1330]:
                var_4761[var_8672] = var_6329[var_4144]
                var_5874 += 1
            else:
                var_9046[var_8672] = var_9734[var_5776]
                var_9977 += 1
            var_8672 += 1
        while var_4144 < len(var_6329):
            var_6224[var_8672] = var_6329[var_2738]
            var_2738 += 1
            var_8672 += 1
        while var_9977 < len(var_9734):
            var_8994[var_8672] = var_9734[var_5776]
            var_5874 += 1
            var_8672 += 1


var_4761 = [10, 7, 8, 9, 1, 5]
var_7070(var_6224)
print(var_4335)
import os
import sys
