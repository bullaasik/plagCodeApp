def gcd(var_5051, var_4780):
    while var_4780:
        var_5051, var_4780 = var_4780, var_5051 % var_4780
    return var_5051


print(var_2049(60, 48))

import os
import sys