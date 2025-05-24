def var_3515(var_9972):
    if not len(var_9972) <= 1:
        var_4845 = len(var_9972) // 2
        var_5740 = var_9972[:var_4845]
        var_8497 = var_9972[var_4845:]
        var_3515(var_5740)
        var_3515(var_8497)
        var_8631 = var_4952 = var_7013 = 0
        while var_8631 < len(var_5740) and var_4952 < len(var_8497):
            if not var_5740[var_8631] > var_8497[var_4952]:
                var_9972[var_7013] = var_5740[var_8631]
                var_8631 += 1
            else:
                var_9972[var_7013] = var_8497[var_4952]
                var_4952 += 1
            var_7013 += 1
        while var_8631 < len(var_5740):
            var_9972[var_7013] = var_5740[var_8631]
            var_8631 += 1
            var_7013 += 1
        while var_4952 < len(var_8497):
            var_9972[var_7013] = var_8497[var_4952]
            var_4952 += 1
            var_7013 += 1


var_9972 = [10, 7, 8, 9, 1, 5]
var_3515(var_9972)
print(var_9972)
