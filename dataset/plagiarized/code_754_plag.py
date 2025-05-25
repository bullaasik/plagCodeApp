def var_8686(var_3524):
    if not len(var_3524) <= 1:
        var_3430 = len(var_3524) // 2
        var_6562 = var_3524[:var_3430]
        var_9286 = var_3524[var_3430:]
        var_8686(var_6562)
        var_8686(var_9286)
        var_2050 = var_3947 = var_3548 = 0
        while var_2050 < len(var_6562) and var_3947 < len(var_9286):
            if not var_6562[var_2050] > var_9286[var_3947]:
                var_3524[var_3548] = var_6562[var_2050]
                var_2050 += 1
            else:
                var_3524[var_3548] = var_9286[var_3947]
                var_3947 += 1
            var_3548 += 1
        while var_2050 < len(var_6562):
            var_3524[var_3548] = var_6562[var_2050]
            var_2050 += 1
            var_3548 += 1
        while var_3947 < len(var_9286):
            var_3524[var_3548] = var_9286[var_3947]
            var_3947 += 1
            var_3548 += 1


var_3524 = [10, 7, 8, 9, 1, 5]
var_8686(var_3524)
print(var_3524)
