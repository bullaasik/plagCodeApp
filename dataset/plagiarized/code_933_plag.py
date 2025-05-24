def var_6231(var_7379):
    var_2146 = 1
    while var_2146 < len(var_7379):
        var_5821 = var_7379[var_2146]
        var_4550 = var_2146 - 1
        while var_4550 >= 0 and var_7379[var_4550] > var_5821:
            var_7379[var_4550 + 1] = var_7379[var_4550]
            var_4550 -= 1
        var_7379[var_4550 + 1] = var_5821
        var_2146 += 1


var_7379 = [64, 34, 25, 12, 22, 11, 90]
var_6231(var_7379)
print(var_7379)
