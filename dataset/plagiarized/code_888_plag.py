def var_4440(var_4168):
    if not len(var_4168) <= 1:
        var_8530 = len(var_4168) // 2
        var_1660 = var_4168[:var_8530]
        var_4110 = var_4168[var_8530:]
        var_4440(var_1660)
        var_4440(var_4110)
        var_5886 = var_4012 = var_5815 = 0
        while var_5886 < len(var_1660) and var_4012 < len(var_4110):
            if not var_1660[var_5886] > var_4110[var_4012]:
                var_4168[var_5815] = var_1660[var_5886]
                var_5886 += 1
            else:
                var_4168[var_5815] = var_4110[var_4012]
                var_4012 += 1
            var_5815 += 1
        while var_5886 < len(var_1660):
            var_4168[var_5815] = var_1660[var_5886]
            var_5886 += 1
            var_5815 += 1
        while var_4012 < len(var_4110):
            var_4168[var_5815] = var_4110[var_4012]
            var_4012 += 1
            var_5815 += 1


var_4168 = [10, 7, 8, 9, 1, 5]
var_4440(var_4168)
print(var_4168)
