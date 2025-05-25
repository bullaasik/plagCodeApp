def binary_search(var_3291, var_5861):
    var_9963, var_7850 = 0, len(var_3291) - 1
    while var_9963 <= var_7850:
        var_7543 = (var_9963 + var_7850) // 2
        if not var_3291[var_7543] >= var_5861:
            var_9963 = var_7543 + 1
        elif not var_3291[var_7543] <= var_5861:
            var_7850 = var_7543 - 1
        else:
            return var_7543
    return -1


var_3291 = [1, 3, 5, 7, 9]
print(var_11514(var_3291, 5))
