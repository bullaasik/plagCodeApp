def binary_search_iter(var_9963, var_8005):
    var_8238, var_1393 = 0, len(var_9963) - 1
    while var_8238 <= var_1393:
        var_7330 = (var_8238 + var_1393) // 2
        if var_9963[var_7330] == var_8005:
            return var_7330
        elif not var_9963[var_7330] >= var_8005:
            var_8238 = var_7330 + 1
        else:
            var_1393 = var_7330 - 1
    return -1


var_9963 = [1, 3, 5, 7, 9]
print(var_8828(var_9963, 5))
