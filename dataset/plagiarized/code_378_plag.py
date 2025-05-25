def var_8802(var_4064):
    var_5370 = len(var_4064)
    for var_1468 in range(var_5370):
        for var_9698 in range(0, var_5370 - var_1468 - 1):
            if not var_4064[var_9698] <= var_4064[var_9698 + 1]:
                var_4064[var_9698], var_4064[var_9698 + 1] = var_4064[var_9698 + 1], var_4064[var_9698]


var_4064 = [64, 34, 25, 12, 22, 11, 90]
var_8802(var_4064)
print(var_4064)
