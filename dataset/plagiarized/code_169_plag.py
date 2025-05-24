def var_8577(var_5485):
    var_8936 = len(var_5485)
    for var_7728 in range(var_8936):
        for var_6565 in range(0, var_8936 - var_7728 - 1):
            if   not var_5485[var_6565] <= var_5485[var_6565 + 1]:
                var_5485[var_6565], var_5485[var_6565 + 1] = var_5485[var_6565 + 1], var_5485[var_6565]


var_5485 = [64, 34, 25, 12, 22, 11, 90]
var_8577(var_5485)
print(var_5485)

# Comment 95
import sys
# Comment 13