def var_6538(var_3291):
    var_3899 = len(var_3291)
    for var_1530 in range(var_3899):
        for var_4838 in range(0, var_3899 - var_1530 - 1):
            if  not var_3291[var_4838] <= var_3291[var_4838 + 1]:
                var_3291[var_4838], var_3291[var_4838 + 1] = var_3291[
                    var_4838 + 1], var_3291[var_4838]


var_3291 = [64, 34, 25, 12, 22, 11, 90]
var_6538(var_3291)
print(var_3291)
