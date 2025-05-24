def var_4852(var_6840):
    if var_6840 == 0:
        return 1
    sub_var_4852_8276(var_6840)


def sub_var_4852_8276(var_6840):
    return var_6840 * var_4852(var_6840 - 1)


print(var_4852(5))

# Comment 4
import sys
import math