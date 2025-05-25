def var_5354(var_1659, var_3907):
    while var_3907:
        var_1659, var_3907 = var_3907, var_1659 % var_3907
    return var_1659


print(var_5354(60, 48))

import os