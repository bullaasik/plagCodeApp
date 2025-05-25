def var_3087(var_9119):
    if var_9119 == 0:
        return 1
    return var_9119 * var_3087(var_9119 - 1)


print(var_3087(5))
import sys
