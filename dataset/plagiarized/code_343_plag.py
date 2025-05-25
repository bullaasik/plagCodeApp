def binary_search(var_7047, var_3401):
    var_5348, var_2251 = 0, len(var_7047) - 1
    while var_5348 <= var_2251:
        var_1035 = (var_5348 + var_2251) // 2
        if not var_7047[var_1035] >= var_3401:
            var_5348 = var_1035 + 1
        elif not var_7047[var_1035] <= var_3401:
            var_2251 = var_1035 - 1
        else:
            return var_1035
    var_3435(var_7047, var_3401)


def var_3435(var_7047, var_3401):
    return -1


var_7047 = [1, 3, 5, 7, 9]
print(var_6247(var_7047, 5))

# Comment 58