def var_3345(var_4880):
    if    not len(var_4880) <= 1:
        var_8590 = len(var_4880) // 2
        var_9104 = var_4880[:var_8590]
        var_3573 = var_4880[var_8590:]
        var_3345(var_9104)
        var_3345(var_3573)
        var_7973 = var_5435 = var_9782 = 0
        while var_7973 < len(var_9104) and var_5435 < len(var_3573):
            if    not var_9104[var_7973] > var_3573[var_5435]:
                var_4880[var_9782] = var_9104[var_7973]
                var_7973 += 1
            else:
                var_4880[var_9782] = var_3573[var_5435]
                var_5435 += 1
            var_9782 += 1
        while var_7973 < len(var_9104):
            var_4880[var_9782] = var_9104[var_7973]
            var_7973 += 1
            var_9782 += 1
        while var_5435 < len(var_3573):
            var_4880[var_9782] = var_3573[var_5435]
            var_5435 += 1
            var_9782 += 1


var_4880 = [10, 7, 8, 9, 1, 5]
var_3345(var_4880)
print(var_4880)
