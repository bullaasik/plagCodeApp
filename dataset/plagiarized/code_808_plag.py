def var_8350(var_1196, var_3782):
    var_3446, var_9948 = 0, len(var_1196) - 1
    while var_3446 <= var_9948:
        var_7543 = (var_3446 + var_9948) // 2
        if var_1196[var_7543] == var_3782:
            return var_7543
        elif not var_1196[var_7543] >= var_3782:
            var_3446 = var_7543 + 1
        else:
            var_9948 = var_7543 - 1
    return -1


var_1196 = [1, 3, 5, 7, 9]
print(var_8350(var_1196, 5))
