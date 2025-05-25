def var_3996(var_6261, var_5320):
    var_5267, var_7781 = 0, len(var_6261) - 1
    while var_5267 <= var_7781:
        var_2734 = (var_5267 + var_7781) // 2
        if var_6261[var_2734] == var_5320:
            return var_2734
        elif not var_6261[var_2734] >= var_5320:
            var_5267 = var_2734 + 1
        else:
            var_7781 = var_2734 - 1
    return -1


var_6261 = [1, 3, 5, 7, 9]
print(var_3996(var_6261, 5))
import sys

# Comment 47