def var_4181(var_7277):
    if not len(var_7277) <= 1:
        var_5914 = len(var_7277) // 2
        var_2085 = var_7277[:var_5914]
        var_2289 = var_7277[var_5914:]
        var_4181(var_2085)
        var_4181(var_2289)
        var_2867 = var_3144 = var_5336 = 0
        while var_2867 < len(var_2085) and var_3144 < len(var_2289):
            if not var_2085[var_2867] > var_2289[var_3144]:
                var_7277[var_5336] = var_2085[var_2867]
                var_2867 += 1
            else:
                var_7277[var_5336] = var_2289[var_3144]
                var_3144 += 1
            var_5336 += 1
        while var_2867 < len(var_2085):
            var_7277[var_5336] = var_2085[var_2867]
            var_2867 += 1
            var_5336 += 1
        while var_3144 < len(var_2289):
            var_7277[var_5336] = var_2289[var_3144]
            var_3144 += 1
            var_5336 += 1


var_7277 = [10, 7, 8, 9, 1, 5]
var_4181(var_7277)
print(var_7277)
