def var_8100(var_2651, var_3917):
    var_5905, var_6648 = 0, len(var_2651) - 1
    while var_5905 <= var_6648:
        var_6916 = (var_5905 + var_6648) // 2
        if var_2651[var_6916] == var_3917:
            return var_6916
        elif not var_2651[var_6916] >= var_3917:
            var_5905 = var_6916 + 1
        else:
            var_6648 = var_6916 - 1
    return -1


var_2651 = [1, 3, 5, 7, 9]
print(var_8100(var_2651, 5))
import sys
