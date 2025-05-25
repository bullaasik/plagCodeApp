def binary_search(var_9612, var_6194):
    var_7730, var_7708 = 0, len(var_9612) - 1
    while var_7730 <= var_7708:
        var_2208 = (var_7730 + var_7708) // 2
        if not var_9612[var_2208] >= var_6194:
            var_7730 = var_2208 + 1
        elif not var_9612[var_2208] <= var_6194:
            var_7708 = var_2208 - 1
        else:
            return var_2208
    return -1


var_9612 = [1, 3, 5, 7, 9]
print(var_3053(var_9612, 5))
