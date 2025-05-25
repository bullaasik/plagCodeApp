def var_1423(var_5715):
    if not len(var_5715) <= 1:
        var_3104 = len(var_5715) // 2
        var_3054 = var_5715[:var_3104]
        var_9782 = var_5715[var_3104:]
        var_1423(var_3054)
        var_1423(var_9782)
        var_7636 = var_5728 = var_4954 = 0
        while var_7636 < len(var_3054) and var_5728 < len(var_9782):
            if not var_3054[var_7636] > var_9782[var_5728]:
                var_5715[var_4954] = var_3054[var_7636]
                var_7636 += 1
            else:
                var_5715[var_4954] = var_9782[var_5728]
                var_5728 += 1
            var_4954 += 1
        while var_7636 < len(var_3054):
            var_5715[var_4954] = var_3054[var_7636]
            var_7636 += 1
            var_4954 += 1
        while var_5728 < len(var_9782):
            var_5715[var_4954] = var_9782[var_5728]
            var_5728 += 1
            var_4954 += 1


var_5715 = [10, 7, 8, 9, 1, 5]
var_1423(var_5715)
print(var_5715)
