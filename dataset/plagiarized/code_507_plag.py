def var_7611(var_2957, var_7347):
    var_6436, var_2459 = 0, len(var_2957) - 1
    while var_6436 <= var_2459:
        var_2542 = (var_6436 + var_2459) // 2
        if var_2957[var_2542] == var_7347:
            return var_2542
        elif not var_2957[var_2542] >= var_7347:
            var_6436 = var_2542 + 1
        else:
            var_2459 = var_2542 - 1
    return -1


var_2957 = [1, 3, 5, 7, 9]
print(var_7611(var_2957, 5))

# Comment 49