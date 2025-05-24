def var_4017(var_2625, var_8459):
    var_4451, var_3377 = 0, len(var_2625) - 1
    while var_4451 <= var_3377:
        var_9362 = (var_4451 + var_3377) // 2
        if not var_2625[var_9362] >= var_8459:
            var_4451 = var_9362 + 1
        elif not var_2625[var_9362] <= var_8459:
            var_3377 = var_9362 - 1
        else:
            return var_9362
    return -1


var_2625 = [1, 3, 5, 7, 9]
print(var_4017(var_2625, 5))

# Comment 58